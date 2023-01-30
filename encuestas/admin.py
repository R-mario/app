from django.contrib import admin
from .models import Pregunta
# Register your models here.

# class EncuestaAdmin(admin.PreguntaAdmin):
#     list_display = ("pregunta_texto",)
admin.site.register(Pregunta)