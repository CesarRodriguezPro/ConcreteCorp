from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/signup.html'), name='logout'),
    path('registration_owner/', views.registration_owner, name='registration_owner'),
    path('registration_employees/', views.registration_employees, name='registration_employees'),
    path('profile', views.profile_view, name='profile'),
]