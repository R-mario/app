from django.contrib import admin
from .models import Organism,Habitat,Diet,Behaviour,Reference

# Register your models here.
class OrgAdmin(admin.ModelAdmin):
    list_display = ("common_name","scientific_name",)

class HabAdmin(admin.ModelAdmin):
    list_display = ("environment","location","organism",)

class DietAdmin(admin.ModelAdmin):
    list_display = ("diet","organism",)

class BehaAdmin(admin.ModelAdmin):
    list_display = ("organism","behaviour",)

class RefAdmin(admin.ModelAdmin):
    list_display = ("author","organism",)

admin.site.register(Organism,OrgAdmin)
admin.site.register(Habitat, HabAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(Behaviour, BehaAdmin)
admin.site.register(Reference, RefAdmin)