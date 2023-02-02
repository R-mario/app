from django.db import models

# Create your models here.
class Member(models.Model):
  nombre = models.CharField(max_length=255)
  apellido_1 = models.CharField(max_length=255)
  # correo = models.CharField(max_length=255)
  # pwd = models.CharField(max_length=255)
  # movido a forms

  def __str__(self):
    return f"{self.apellido_1}, {self.nombre}"
