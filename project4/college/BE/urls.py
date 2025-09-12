from django.urls import path
from BE.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]