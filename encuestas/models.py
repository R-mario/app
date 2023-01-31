import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicación')

    @admin.display(
    #"""decorador para mostrar en admin"""
        boolean=True,
        ordering='pub_date',
        description='¿Publicada recientemente?',
    )
    def publicada_recientemente(self):
        return timezone.now() - datetime.timedelta(days =1)<= self.fecha_pub <= timezone.now()

    
    def __str__(self):
        return self.pregunta_texto


class Choice(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    eleccion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.eleccion_texto