from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=4, unique=True)
    flag = models.URLField(blank=True)

    # Additional fields as needed
    population = models.PositiveIntegerField()
    capital = models.CharField(max_length=100)
    

    # Define any other fields you need to represent country data

    def __str__(self):
        return self.name
# In admin.py file of your Django app


def get_countries():
    countries = Country.objects.all()
    return countries
