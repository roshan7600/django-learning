from django.urls import path
from RCB.views import *
app_name='something'

urlpatterns=[
    path('captain/' , captain , name='captain')
]