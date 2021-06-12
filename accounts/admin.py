from django.contrib import admin
from .models import User, Companies, Owner

admin.site.register(Owner)
admin.site.register(User)
admin.site.register(Companies)
