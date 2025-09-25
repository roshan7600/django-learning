from django.contrib import admin

# Register your models here.

from .models import Country, Capital

admin.site.register(Country)
admin.site.register(Capital)