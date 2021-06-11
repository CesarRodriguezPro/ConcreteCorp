from django.db import models
from accounts.models import User


class ErrorSystem(models.Model):
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=225)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.type} {self.location}"


class EventSystem(models.Model):
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=225)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.type} {self.location}"


class LoginEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.user}"

