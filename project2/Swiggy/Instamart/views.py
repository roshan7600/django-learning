from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def chips(request):
    return HttpResponse('There are so many chips in the instamart')

def dairy_milk(request):
    return HttpResponse('In instamart so many flavor of dairy milk')    
    