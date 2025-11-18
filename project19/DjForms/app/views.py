from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def StDjform(request):

    ESTDJF=StudentDjForm()
    d={'ESTDJF':ESTDJF}

    if request.method=='POST':
        SFDO=StudentDjForm(request.POST)
        if SFDO.is_valid():
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
    return render(request,'StDjform.html',d)

