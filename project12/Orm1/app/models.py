from django.db import models

# Create your models here.



class Country(models.Model):
    country_name = models.CharField(max_length=100)
    population = models.BigIntegerField()
    continent = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name


class Capital(models.Model):
    capital_name = models.CharField(max_length=100)
    area_sq_km = models.IntegerField()
    population = models.BigIntegerField()
    country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name="capital")

    def __str__(self):
        return self.capital_name