from django.urls import path
from BBA.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]