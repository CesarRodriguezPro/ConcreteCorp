from django.shortcuts import render
from django.views.generic import View
from .models import EventSystem, ErrorSystem,LoginEvent
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginRequiredMixin, View):
    context = {
        'events': EventSystem.objects.all()[:30],
        'errors': ErrorSystem.objects.all()[:30],
        'logins': LoginEvent.objects.all()[:30],
    }

    def get(self, request):
        return render(request, 'system_log/home.html', self.context)
