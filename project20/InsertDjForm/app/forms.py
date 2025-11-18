from django import forms
from app.models import *

class TopicDjForm(forms.Form):
    Topic_name=forms.CharField()

class WebpageDjForm(forms.Form):
    Topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())  
    name=forms.CharField()  
    Url=forms.URLField()

class AccessRecordDjForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    Author=forms.CharField()
    Date=forms.DateField()
        