from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        ordering = ['apellido']