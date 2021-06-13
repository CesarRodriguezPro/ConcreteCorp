from django.urls import path
from .views import HelloWorldView
app_name = 'api'

urlpatterns = [
    path('auth/', HelloWorldView.as_view(), name='auth')
]