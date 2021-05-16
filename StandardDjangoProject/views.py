from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserArea(LoginRequiredMixin, TemplateView):
    template_name = 'UserArea.html'


class Home(TemplateView):
    template_name = "index.html"



