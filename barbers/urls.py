from django.urls import path
from . import views

urlpatterns = [
    # path('', views.register_login_view, name='index'),
    path('', views.barberPage, name='barberpage'),
    path('createprofile/', views.createprofile, name='barberprofile'), 
    path('editprofile/', views.editprofile, name='editprofile'),
    path('addservices/', views.addservices, name='addservices'),
    # path('profile/<int:id>/', views.barber_detail, name='barber_profile'),
    path('profile/', views.barber_detail, name='barber_profile'),
    path('logout/', views.logoutUser, name='logout'),
    path('createprofile/', views.createprofile, name='createprofile'),
    path('barberservices/', views.barber_services, name='service'),
    path('profilepage/', views.profilepage, name='profilepage'),
    path('dashboard/', views.profilepage, name='profilepage'),
    path('barber/<int:id>/', views.barber_detail, name='barber_detail'),
    path('appointments/', views.user_appointments, name='user_appointments'),
    path('book_appointment/<int:barber_id>/<str:appointment_time>/', views.book_appointment, name='book_appointment'),
    # path('book/<int:barber_id>/', views.book_appointment, name='book_appointment'),
]
