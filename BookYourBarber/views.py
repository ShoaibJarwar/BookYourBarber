from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from users.models import CustomUser


def homePage(request):
    return render(request, 'index.html')

def send_verification_email(user):
    """Send email verification link to the user."""
    token = default_token_generator.make_token(user)
    verification_link = f"http://127.0.0.1:8000{reverse('verify_email', args=[user.pk, token])}"

    send_mail(
        "Verify Your Email - BookYourBarber",
        f"Click the link to verify your email: {verification_link}",
        "bookyourbarber19@gmail.com",
        [user.email],
        fail_silently=False,
    )

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("userType")

        # Check if username or email already exists
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect("register")

        # Password validation
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(request, " ".join(e.messages))  # Show all password errors
            return redirect("register")

        # Create user (inactive by default)
        user = CustomUser.objects.create_user(username=username, email=email, password=password, role=role, is_active=False)
        
        # Send verification email
        send_verification_email(user)

        messages.success(request, "Registration successful! Please check your email to verify your account.")
        return redirect("login")  # Redirect to login page after email verification

    return render(request, "index.html")

def verify_email(request, user_id, token):
    user = get_object_or_404(CustomUser, pk=user_id)

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Email verified successfully! You can now book appointments.")
        return redirect("barberpage" if user.role == "barber" else "user")
    else:
        messages.error(request, "Invalid or expired verification link.")
        return redirect("login")

def loginView(request):
    if request.method == "POST":
        selected_option = request.POST.get("userType")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)

        if user is not None and user.role == selected_option:
            login(request, user)
            return redirect('barberpage' if user.role == "barber" else 'user')
        else:
            messages.error(request, "Wrong Credentials!" if user is None else "No such User in this UserType")
            return render(request, "login.html")

    return render(request, "login.html")




