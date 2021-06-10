from django.shortcuts import render, redirect
from .forms import OwnerCreateForm, EmployeesCreateForm, CompaniesCreateForm
from django.contrib import messages
from .models import User
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login


class LoginView(View):

    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("private_area:home")
        else:
            messages.error(request, "wrong login Please Try Again")
            return render(request, 'accounts/login.html')


class RegistrationOwner(View):

    def get(self, request):
        context = {
            "is_owner": True
        }
        return render(request, "accounts/register.html", context)

    def post(self, request):

        ## working in this area.
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeatPassword']

        if password == repeat_password:

            owner = User.objects.get(username=user_form.cleaned_data['username'])
            company_.owner = owner
            company_.save()

            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")


class RegistrationEmployee(LoginRequiredMixin, View):
    def get(self, request):
        user_form = EmployeesCreateForm()
        context = {
            'title': 'Sign up Employees',
            'form': user_form,
        }
        return render(request, "accounts/signup.html", context)

    def post(self, request):
        user_form = EmployeesCreateForm(request.POST)
        if user_form.is_valid():
            user_ = user_form.save(commit=False)
            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"
