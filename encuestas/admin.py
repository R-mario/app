from django.contrib import admin
from .models import Pregunta,Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    """muestra los valores de choice y 3 espacios extra"""
    model = Choice
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pregunta_texto']}),
        ('Información de Fecha', {'fields': ['fecha_pub'],
                                  'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # muestra elecciones para cada pregunta
    list_display = ('pregunta_texto','fecha_pub','publicada_recientemente',)# estos campos junto a cada registro
    list_filter = ['fecha_pub']
    search_fields = ['pregunta_texto']



admin.site.register(Pregunta, PreguntaAdmin)
# admin.site.register(Choice)

