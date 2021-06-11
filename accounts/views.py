from django.shortcuts import render, redirect
from .forms import EmployeesCreateForm
from django.contrib import messages
from .models import User, Owner, Companies, Employee
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import password_validators_help_texts, validate_password
from system_log.models import LoginEvent


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

    context = {
        "is_owner": True,
        'help_text': password_validators_help_texts(),
    }

    def get(self, request):
        return render(request, "accounts/register.html", self.context)

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeatPassword']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        company_name = request.POST['company_name']
        company_address = request.POST['address']

        if password and repeat_password and password == repeat_password:
            user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            owner = Owner(profile=user)
            owner.save()
            company = Companies(owner=owner, company_name=company_name, address=company_address)
            company.save()
            messages.success(request, 'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")

        messages.error(request, 'Password Do Not Match')
        return render(request, "accounts/register.html", self.context)


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
