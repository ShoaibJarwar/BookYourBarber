from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class BarberProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name="barber_profile")
    full_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='barber_profiles/', blank=True, null=True)
    shop_name = models.CharField(max_length=255)
    location = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    # professional_email = models.EmailField(unique=True)
    shop_banner = models.ImageField(upload_to='shop_banners/', blank=True, null=True)
    available_time_slots = models.CharField(max_length=255, help_text="Example: 10:00 AM - 4:00 PM")

    def __str__(self):
        return self.full_name

class Service(models.Model):
    barber = models.ForeignKey(BarberProfile, on_delete=models.CASCADE, related_name="services")
    service_name = models.CharField(max_length=255)
    service_image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.service_name} - {self.barber.shop_name}"



class CustomUser(AbstractUser):
    is_barber = models.BooleanField(default=False)  # Flag to identify barbers

class Barber(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='barber')
    shop_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='barber_profiles/', blank=True, null=True)

    def __str__(self):
        return self.shop_name
