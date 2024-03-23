from django.db import models
from django.contrib.auth.models import User
import numpy, pandas


# Create your models here.

class Ingreso(models.Model):
     
    fecha= models.DateField()
    importe= models.IntegerField()
    categoria = models.CharField(max_length=60)
    descripcion= models.CharField(max_length=60)

    def __str__(self):
        return f' Fecha: {self.fecha}  {self.descripcion}  $ {self.importe}'

class Egreso(models.Model):
    
    fecha= models.DateField()
    importe= models.IntegerField()
    categoria = models.CharField(max_length=60)
    descripcion= models.CharField(max_length=60)

    def __str__(self):
        return f'{self.descripcion} se ha contabilizado con éxito'

class Cuenta(models.Model):

    tipo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return f"Nombre:{self.nombre}"

class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    
    

