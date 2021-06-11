from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Owner(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)


class Companies(models.Model):
    owner = models.ForeignKey(to=Owner, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, unique=True, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    STATUS_CHOICES = [
        ("Admin", "Admin"),
        ("Manager", "Manager"),
        ("sysAdmin", "System Admin"),
        ("Employee", "Employee"),
    ]
    role = models.CharField(choices=STATUS_CHOICES, max_length=10, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)

