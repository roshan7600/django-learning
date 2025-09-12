from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Branch(request):
    return HttpResponse('This is the branch of MBA')
