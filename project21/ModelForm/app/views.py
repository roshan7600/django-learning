from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.

def insert_Topic_by_MF(request):
    d={'ETMFO':TopicMF()}
    if request.method=='POST':
        TMFDO=TopicMF(request.POST)
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse('Topic is create sucessfully')
        else:
            return HttpResponse('Topic is already exist')    
    return render(request,'insert_Topic_by_MF.html',d)        

    