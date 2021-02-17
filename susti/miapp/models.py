from django.db import models

# Create your models here.

class Region(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(default='null')
    cases = models.CharField(max_length=50)
    deaths = models.CharField(max_length=50)
    lathality = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    image = models.ImageField(default='null')
    state = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)