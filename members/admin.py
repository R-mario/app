from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido_1",)

admin.site.register(Member,MemberAdmin)