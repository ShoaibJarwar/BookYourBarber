from django.contrib.auth.models import AbstractUser
from django.conf import settings
from barbers.models import BarberProfile 
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('user', 'User'),
        ('barber', 'Barber'),
    )
    role = models.CharField(max_length=10, choices=USER_TYPES, default='user')


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set', 
        blank=True
    )

    def __str__(self):
        return self.username


class Barber(models.Model):
    full_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    services_title = models.CharField(max_length=255) 


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.barber.full_name} on {self.appointment_time}"
    



class ClientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="client_profile"
    )
    full_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='client_profiles/', blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    # preferred_location = models.TextField(blank=True, null=True)
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    # email = models.EmailField(unique=True)

    def __str__(self):
        return self.full_name
