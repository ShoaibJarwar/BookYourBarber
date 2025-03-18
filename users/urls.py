from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('profile/', views.client_profile, name='client_profile'),
    path('search/', views.search_barbers, name='search_barbers'),
    path('book_appointment/<int:barber_id>/', views.book_appointment, name='book_appointment'),
    path('appointments/cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),

]