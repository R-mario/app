from django.urls import path
from . import views

urlpatterns = [
    path('', views.organism_list, name = "main"), #página principal 
    path('detail/', views.organism_detail,name = "detail")
]