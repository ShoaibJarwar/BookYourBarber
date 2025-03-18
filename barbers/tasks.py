from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task
def send_email_reminder(email, barber_name, subject):
    message = f"Reminder: Your appointment with {barber_name} is coming up soon!"
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
