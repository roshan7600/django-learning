from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain (request):
    return HttpResponse('CSK cpatain is MSD')

