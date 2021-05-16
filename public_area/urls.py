from django.urls import path

from . import views

app_name = 'public_area'

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]