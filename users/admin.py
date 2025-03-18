from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Appointment, ClientProfile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Appointment)
admin.site.register(ClientProfile)
