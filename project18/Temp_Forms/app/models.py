from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=50 ,primary_key=True)

    def __str__(self):
        return self.Topic_name
    
class Webpage(models.Model):
    Topic_name=models.ForeignKey(Topic , on_delete=models.CASCADE)   
    name=models.CharField(max_length=50)
    Url=models.URLField()

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage , on_delete=models.CASCADE)
    Author=models.CharField(max_length=50)
    Date=models.DateField()

    def __str__(self):
        return self.Author