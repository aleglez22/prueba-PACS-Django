from django.db import models

class Person(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.BigIntegerField()
    time = models.DateTimeField()
    apellido = models.CharField( max_length=50)
    direccion = models.CharField( max_length=100,default="calle")
    domicilio = models.CharField(max_length=50,default="centro")

