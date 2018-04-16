from django.db import models
from django.contrib.postgres.fields import ArrayField

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    #FileField option for images
    #images = models.ManyToManyField(
    rating = models.FloatField()
    description = models.CharField(max_length= 500)
    tags = ArrayField(models.CharField(max_length=50))


