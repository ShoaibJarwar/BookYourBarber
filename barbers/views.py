# from django.shortcuts import render, redirect
# from django.contrib import messages

# def register_login_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user_type = form.cleaned_data['user_type']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             # Check if user already exists
#             if User.objects.filter(username=username).exists():
#                 return render(request, 'index.html', {'form': form, 'error': 'Username already exists'})

#             # Create user
#             user = User.objects.create_user(username=username, email=email, password=password)
            
#             # Auto-login user after registration
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)

#             # Redirect to the appropriate page
#             if user_type == 'barber':
#                 return redirect('barberpage')  # Ensure 'barberpage' exists in urls.py
#             else:
#                 return redirect('userpage')  # Ensure 'userpage' exists in urls.py
#     else:
#         form = RegisterForm()

#     return render(request, 'index.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BarberProfile, Service
from django.contrib.auth import logout
from barbers.models import BarberProfile
from users.models import Appointment
from django.utils.timezone import now
from users.models import Barber

@login_required
def createprofile(request):
    """Handles barber profile creation."""
    try:
        profile = BarberProfile.objects.get(user=request.user)
    except BarberProfile.DoesNotExist:
        profile = None

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        shop_name = request.POST.get("shop_name")
        location = request.POST.get("location")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        phone_number = request.POST.get("phone_number")
        # professional_email = request.POST.get("professional_email")
        available_time_slots = request.POST.get("available_time_slots")

        profile_picture = request.FILES.get("profile_picture")
        shop_banner = request.FILES.get("shop_banner")

        if not latitude or not longitude:
            messages.error(request, "Please select a valid location on the map.")
            return render(request, "createprofile.html")

    
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            messages.error(request, "Invalid latitude or longitude format.")
            return render(request, "createprofile.html")


        if profile:
        
            profile.full_name = full_name
            profile.shop_name = shop_name
            profile.location = location
            profile.latitude = latitude
            profile.longitude = longitude
            profile.phone_number = phone_number
            # profile.professional_email = professional_email
            profile.available_time_slots = available_time_slots

            if profile_picture:
                profile.profile_picture = profile_picture
            if shop_banner:
                profile.shop_banner = shop_banner

            profile.save()
            messages.success(request, "Profile updated successfully!")
        else:
        
            BarberProfile.objects.create(
                user=request.user,
                full_name=full_name,
                shop_name=shop_name,
                location=location,
                latitude=latitude,
                longitude=longitude,
                phone_number=phone_number,
                # professional_email=professional_email,
                available_time_slots=available_time_slots,
                profile_picture=profile_picture,
                shop_banner=shop_banner,
            )
            messages.success(request, "Profile created successfully!")

        return redirect("profilepage")

    return render(request, "createprofile.html")


@login_required
def editprofile(request):
    """Handles barber profile updates."""
    try:
        profile = BarberProfile.objects.get(user=request.user)
    except BarberProfile.DoesNotExist:
        profile = None

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        shop_name = request.POST.get("shop_name")
        location = request.POST.get("location")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        phone_number = request.POST.get("phone_number")
        # professional_email = request.POST.get("professional_email")
        available_time_slots = request.POST.get("available_time_slots")

        profile_picture = request.FILES.get("profile_picture")
        shop_banner = request.FILES.get("shop_banner")

        if not latitude or not longitude:
            messages.error(request, "Please select a valid location on the map.")
            return render(request, "createprofile.html")

    
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            messages.error(request, "Invalid latitude or longitude format.")
            return render(request, "createprofile.html")


        if profile:
        
            profile.full_name = full_name
            profile.shop_name = shop_name
            profile.location = location
            profile.latitude = latitude
            profile.longitude = longitude
            profile.phone_number = phone_number
            # profile.professional_email = professional_email
            profile.available_time_slots = available_time_slots

            if profile_picture:
                profile.profile_picture = profile_picture
            if shop_banner:
                profile.shop_banner = shop_banner

            profile.save()
            messages.success(request, "Profile updated successfully!")
        else:
        
            BarberProfile.objects.create(
                user=request.user,
                full_name=full_name,
                shop_name=shop_name,
                location=location,
                latitude=latitude,
                longitude=longitude,
                phone_number=phone_number,
                # professional_email=professional_email,
                available_time_slots=available_time_slots,
                profile_picture=profile_picture,
                shop_banner=shop_banner,
            )
            messages.success(request, "Profile created successfully!")

        return redirect("profilepage")

    return render(request, "editprofile.html")


@login_required
def addservices(request):
    if request.method == "POST":
        service_name = request.POST.get("service_name")
        service_image = request.FILES.get("service_image")
        price = request.POST.get("price")

        try:
            barber_profile = BarberProfile.objects.get(user=request.user)
        except BarberProfile.DoesNotExist:
            messages.error(request, "You need to create a profile first!")
            return redirect("profilepage")  

        Service.objects.create(
            barber=barber_profile,
            service_name=service_name,
            service_image=service_image,
            price=price
        )

        return redirect("profilepage")  # Redirect after adding

    return render(request, "services.html")

@login_required
def barberPage(request):
    return render(request, 'barberpage.html')


@login_required
# def barber_detail(request):
#     if not request.user.is_authenticated:
#         return redirect('login') 

#     try:
#         barber_profile = BarberProfile.objects.get(user=request.user) 
#     except BarberProfile.DoesNotExist:
#         return redirect('createprofile') 

#     return render(request, 'barber_detail.html', {'barber': barber_profile})





def barber_detail(request, id=None):
    if id is None:
        if request.user.is_authenticated and hasattr(request.user, 'barber_profile'):
            barber = request.user.barber_profile  
        else:
            return render(request, 'error.html', {'message': 'You do not have a barber profile.'})
    else:
        barber = get_object_or_404(BarberProfile, id=id)

    return render(request, 'barber_detail.html', {'barber': barber})


@login_required
def user_appointments(request):
    """Fetches the latest appointment of the logged-in user and displays it."""
    appointment = Appointment.objects.filter(user=request.user).order_by('-appointment_time').first()
    return render(request, 'user_appointments.html', {'appointment': appointment})

@login_required
def book_appointment(request, barber_id, appointment_time):
    """Creates a new appointment for the logged-in user with a given barber and time."""
    barber = get_object_or_404(BarberProfile, id=barber_id)
    
    # Check if the user already has an appointment at the same time
    existing_appointment = Appointment.objects.filter(user=request.user, appointment_time=appointment_time).exists()
    
    if existing_appointment:
        return render(request, 'error.html', {'message': 'You already have an appointment at this time.'})
    
    # Create and save the appointment
    appointment = Appointment.objects.create(
        user=request.user,
        barber=barber,
        appointment_time=appointment_time
    )
    
    return redirect('user_appointments')  # Redirect to user's appointment page

# def book_appointment(request, barber_id):
#     barber = get_object_or_404(BarberProfile, id=barber_id)
#     return render(request, 'book_appointment.html', {'barber': barber})

@login_required
def barber_services(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    try:
        barber_profile = BarberProfile.objects.get(user=request.user)
        services = Service.objects.filter(barber=barber_profile)
    except BarberProfile.DoesNotExist:
        return redirect('createprofile') 

    return render(request, 'barber_services.html', {'barber': barber_profile, 'services': services})

@login_required
def profilepage(request):
    return render(request, 'profilepage.html')

@login_required
def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    request.session.flush()
    return redirect("/login")

