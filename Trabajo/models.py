from unittest.util import _MAX_LENGTH
from django.db import models

class familiar ( models.Model):
    nombre = models.CharField( max_length = 100)
    parentesco = models.CharField( max_length = 50)
    ocupacion = models.CharField( max_length = 50)
    DNI = models.IntegerField()
    edad = models.IntegerField()

    def __str__(self):
        return f'{self.nombre}, {self.DNI}, {self.id}'

# Create your models here.
