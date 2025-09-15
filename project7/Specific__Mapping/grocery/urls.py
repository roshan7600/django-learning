from django.urls import path
from grocery.views import *
app_name='grocery'

urlpatterns=[
    path('Almond/' , Almond , name='Almond'),
]
