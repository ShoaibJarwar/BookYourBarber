from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from users.models import Appointment
from barbers.models import BarberProfile
from .models import ClientProfile
from django.views.decorators.cache import never_cache
from django.utils.dateparse import parse_datetime
from django.utils.timezone import now, localtime, make_aware

# from .models import Barber


# Create your views here.

@never_cache  
@login_required  
def user(request):
    return render(request, 'user.html')

# def find_nearby_barbers(request):
#     query = request.GET.get('search', '')
#     barbers = Barber.objects.filter(location__icontains=query) if query else Barber.objects.all()

#     return render(request, 'find_nearby_barbers.html', {'barbers': barbers, 'query': query})


@login_required
def user_appointments(request):
    """Fetch the latest appointment of the user and calculate the remaining time correctly."""
    appointment = Appointment.objects.filter(user=request.user).order_by('-appointment_time').first()

    remaining_time_seconds = None  # Default value
    if appointment:
        # Ensure appointment_time is timezone-aware
        if appointment.appointment_time.tzinfo is None:
            appointment_time = make_aware(appointment.appointment_time)  # Convert naive datetime to aware
        else:
            appointment_time = localtime(appointment.appointment_time)

        current_time = localtime(now())

        print(f"Appointment Time: {appointment_time}")  # Debugging
        print(f"Current Time: {current_time}")  # Debugging

        remaining_time = appointment_time - current_time

        if remaining_time.total_seconds() > 0:
            remaining_time_seconds = int(remaining_time.total_seconds())  # Convert to seconds
        else:
            remaining_time_seconds = 0  # If time has already passed

    return render(request, 'user_appointments.html', {
        'appointment': appointment,
        'remaining_time': remaining_time_seconds,
    })


@login_required
def cancel_appointment(request, appointment_id):
    """Allows a user to cancel an appointment."""
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    
    if request.method == "POST":
        appointment.delete()
        messages.success(request, "Your appointment has been canceled successfully.")
        return redirect('user_appointments')

    return redirect('user_appointments')

@login_required
def book_appointment(request, barber_id):
    barber = get_object_or_404(BarberProfile, id=barber_id)

    existing_appointment = Appointment.objects.filter(user=request.user, appointment_time__gte=now()).exists()

    if existing_appointment:
        return render(request, 'error.html', {'message': 'You already have an appointment! Cancel it before booking a new one.'})

    if request.method == 'POST':
        appointment_time = request.POST.get('appointment_time')
        appointment_time = parse_datetime(appointment_time)

        if not appointment_time:
            messages.error(request, "Invalid appointment time.")
            return redirect('book_appointment', barber_id=barber_id)

        Appointment.objects.create(
            user=request.user,
            barber=barber,
            appointment_time=appointment_time
        )

        messages.success(request, "Appointment booked successfully!")
        return redirect('user_appointments')

    return render(request, 'book_appointment.html', {'barber': barber})


def search_barbers(request):
    query = request.POST.get('query', '').strip() 
    matched_barbers = BarberProfile.objects.filter(location__icontains=query)

    return render(request, 'search_barbers.html', {'barbers': matched_barbers, 'query': query})




@login_required
def client_profile(request):
    client_profile, created = ClientProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        client_profile.full_name = request.POST.get("full_name", client_profile.full_name)
        client_profile.phone_number = request.POST.get("phone_number", client_profile.phone_number)
        # client_profile.preferred_location = request.POST.get("preferred_location", client_profile.preferred_location)
        # client_profile.email = request.POST.get("email", client_profile.email)

        if "profile_picture" in request.FILES:
            client_profile.profile_picture = request.FILES["profile_picture"]

        client_profile.save()
        messages.success(request, "Profile Created successfully!")
        return redirect("user")

    return render(request, "client_profile.html", {"client": client_profile})



def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    request.session.flush()
    return redirect("/login")