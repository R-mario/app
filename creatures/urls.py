from django.urls import path
from . import views
# /creatures/ --> muestra los organismos
# /detail/ --> muestra el detalle del organismo id
urlpatterns = [
    path('', views.organism_list, name = "main"), #página principal 
    path('detail/<int:id>', views.organism_detail,name = "detail")
]