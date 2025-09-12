from django.urls import path
from MBA.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]