from django.urls import path
from food.views import *

app_name='food'

urlpatterns=[
    path('items/' ,items  , name='items'),
]