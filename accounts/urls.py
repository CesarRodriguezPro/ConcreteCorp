from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/signup.html'), name='logout'),
    path('registration_owner/', views.RegistrationOwner.as_view(), name='registration_owner'),
    path('registration_employees/', views.RegistrationEmployee.as_view(), name='registration_employees'),
    path('profile', views.ProfileView.as_view(), name='profile'),
]