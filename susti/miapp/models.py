from django.db import models

# Create your models here.

class Region(models.Model):
    date = models.DateTimeField(auto_now_add=False, verbose_name="Fecha")
    name = models.CharField(max_length=100, verbose_name="Nombre de la region")
    image = models.ImageField(default='null', verbose_name="Mapa", upload_to="regiones")
    cases = models.CharField(max_length=50, verbose_name="Casos")
    deaths = models.CharField(max_length=50, verbose_name="Muertes")
    lathality = models.CharField(max_length=50, verbose_name="Letalidad")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"
        ordering = ['id']
    
    def __str__(self):
        return f"{self.name}, Casos: {self.cases}"
    

class Employee(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Nombre completo")
    job = models.CharField(max_length=100, verbose_name="Trabajo")
    image = models.ImageField(default='null', verbose_name="Foto de perfil")
    state = models.BooleanField(verbose_name="Estado")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['id']

    def __str__(self):
        return f"{self.fullname}, Puesto: {self.job} - {self.state}"
    