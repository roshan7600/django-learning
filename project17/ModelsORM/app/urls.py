from django.urls import path
from . import views

urlpatterns = [
    path('all_chai/', views.all_chai, name='all_chai'),
    path('chai/<int:chai_id>/', views.chai_details, name='chai_details'),
]
