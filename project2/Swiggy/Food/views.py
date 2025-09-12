from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Briyani(request):
    return HttpResponse('Spiciy briyani')

def Kabab(request):
    return HttpResponse('There are different types of Kabab') 