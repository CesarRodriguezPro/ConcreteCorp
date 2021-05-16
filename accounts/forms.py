from .models import Companies, User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class OwnerCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'image')
        model = User
        widgets = {'is_owner': forms.HiddenInput()}


class EmployeesCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'image')
        model = User


class CompaniesCreateForm(forms.ModelForm):
    class Meta:
        fields = ('company_name', 'address')
        model = Companies
