from django.views import View
from django.shortcuts import render


#  Public Area

class Home(View):
    def get(self, request):
        return render(request, 'public_area/index.html')
