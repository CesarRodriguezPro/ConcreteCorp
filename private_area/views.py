from django.shortcuts import render
from django.views.generic import View


#  Private Area Views

class Home(View):
    def get(self, request):
        return render(request, 'private_area/index.html')

