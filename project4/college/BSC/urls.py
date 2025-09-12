from django.urls import path
from BSC.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]