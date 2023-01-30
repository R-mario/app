import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicación')

    def publicada_recientemente(self):
        return self.fecha_pub >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.pregunta_texto


class Choice(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    eleccion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.eleccion_texto