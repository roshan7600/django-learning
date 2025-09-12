from django.urls import path
from BTECH.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]