from django.contrib import admin

# Register your models here.
from app.models import *

# CUSTOMIZE ADMIN PANNEL

admin.site.register(Topic)
admin.site.register(Webpage)    
admin.site.register(AccessRecord)