from django.urls import path
from MSC.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]