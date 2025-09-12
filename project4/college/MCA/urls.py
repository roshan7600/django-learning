from django.urls import path
from MCA.views import *
app_name='something'

urlpatterns=[
    path('Branch/' ,Branch  , name='Branch')
]