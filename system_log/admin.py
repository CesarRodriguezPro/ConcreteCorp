from django.contrib import admin
from .models import ErrorSystem, EventSystem, LoginEvent

admin.site.register(ErrorSystem)
admin.site.register(EventSystem)
admin.site.register(LoginEvent)
