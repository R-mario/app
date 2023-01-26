from django.urls import path
from . import views

urlpatterns = [
    path('miembros/', views.todos_miembros, name='todos'),
    path('miembros/detalle/<int:id>', views.miembro, name='detalles'),
    path('testing/', views.testing, name = "testing")
]
