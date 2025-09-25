from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=50 ,primary_key=True)
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic , on_delete=models.CASCADE)   
    name=models.CharField(max_length=50)
    Url=models.URLField()
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage , on_delete=models.CASCADE)
    Author=models.CharField(max_length=50)
    Date=models.DateField()