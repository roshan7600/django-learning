from django.urls import path
from instamart.views import *
app_name='instamart'

urlpatterns=[
    path('ice_cream/' , ice_cream , name='ice_cream'),
]