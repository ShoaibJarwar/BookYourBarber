"""
URL configuration for BookYourBarber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('register/',views.register, name = 'register'),
    path("verify_email/<int:user_id>/<str:token>/", views.verify_email, name="verify_email"),
    path('login/', views.loginView, name = 'loginView'),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),  # ✅ Add this if missing
    path('user/', include('users.urls')),
    path('barber/', include('barbers.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
