from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
# from django.db.models import length

# Insert Topic from user input and display success or exist message throghugh HttpResponse via browser
def insert_topic(request):
    tn=input("Enter Topic Name:")
    TTO=Topic.objects.get_or_create(Topic_name=tn)
    if TTO[1]:
        return HttpResponse("Topic is inserted successfully")
    else:
        return HttpResponse("Topic is already exist")
   

# Display all topics from Topic table and render through template
def display_topics(request):
    LOT=Topic.objects.all()
    return render(request,'display_topics.html',{'LOT':LOT})

 
#Retrieving PTO by using GET method from browser
def insert_Webpage(request):    
    tn=input('enter topic name')
    TO=Topic.objects.get(Topic_name=tn)
    na=input('enter name')
    url=input('enter url')


    TWO=Webpage.objects.get_or_create(Topic_name=TO,name=na,url=url)
    if TWO[1]:
        return HttpResponse('webpage is created')
    else:
        return HttpResponse('webpage is already exists')