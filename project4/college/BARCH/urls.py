from django.urls import path
from BARCH.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]