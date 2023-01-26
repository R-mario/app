from django.contrib import admin

# Register your models here.
class OrgAdmin(admin.ModelAdmin):
    list_display = ("scientific_name", "common_name",)

admin.site.register(Member,OrgAdmin)