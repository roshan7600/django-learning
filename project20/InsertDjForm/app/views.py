from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from app.forms import *

# Create your views here.

def Insert_Topic(request):
    ETDFO=TopicDjForm()
    d={'ETDFO':ETDFO}
    if request.method=='POST':
        TDFDO=TopicDjForm(request.POST)
        if TDFDO.is_valid():
            Tn=TDFDO.changed_data['Topic_name']
            TTO=Topic.objects.get_or_create(Topic_name=Tn)
            if TTO[1]:
                return HttpResponse('Topic is created')
            else:
                return HttpResponse('Topic is already present')
        else:
            return HttpResponse('Invalid data')        


    return render(request,'Insert_Topic.html',d)


def Insert_Webpage(request):
    EWDFO=WebpageDjForm()
    d={'EWDFO':EWDFO}
    if request.method=='POST':
        WDFDO=WebpageDjForm(request.POST)
        if WDFDO.is_valid():
            TO=WDFDO.changed_data['Topic_name']
            name=WDFDO.changed_data['name']
            url=WDFDO.changed_data['Url']
            TWO=Webpage.objects.get_or_create(Topic_name=TO,name=name,URL=url)
            if TWO[1]:
                return  HttpResponse('New Webpage is create')
            else:
                return HttpResponse("Webpage is Already present")    
        else:
            return HttpResponse('invalid Data')        
    return render(request,'Insert_Webpage.html',d)        


