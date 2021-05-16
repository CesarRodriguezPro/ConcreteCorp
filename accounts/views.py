from django.shortcuts import render, redirect
from .forms import OwnerCreateForm, EmployeesCreateForm, CompaniesCreateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User, Companies


def registration_owner(request):
    if request.method == "POST":
        user_form = OwnerCreateForm(request.POST)
        company = CompaniesCreateForm(request.POST)
        if user_form.is_valid() and company.is_valid():
            company_ = company.save(commit=False)
            user_ = user_form.save(commit=False)
            # change the is owner attribute
            user_.is_owner = True
            user_.save()
            # add the owner to the company object
            owner = User.objects.get(username=user_form.cleaned_data['username'])
            company_.owner = owner
            company_.save()

            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")
    else:
        user_form = OwnerCreateForm()
        company = CompaniesCreateForm()

    context = {
        'title': 'Sign up Owner',
        'form': user_form,
        'company': company,
    }
    return render(request, "accounts/signup.html", context)


@login_required()
def registration_employees(request):
    if request.method == "POST":
        user_form = EmployeesCreateForm(request.POST)
        if user_form.is_valid():
            user_ = user_form.save(commit=False)

            messages.success(request, f'Your Account has been Created! You are now able to log in')
            return redirect("accounts:login")
    else:
        user_form = EmployeesCreateForm()

    context = {
        'title': 'Sign up Employees',
        'form': user_form,
    }
    return render(request, "accounts/signup.html", context)


@login_required()
def profile_view(request):
    return render(request, "accounts/profile.html")

