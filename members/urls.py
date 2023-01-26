from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='todos'),
    path('todos/', views.todos_miembros, name = 'todos'),
    path('detalle/<int:id>', views.miembro, name='detalles'),
    path('testing/', views.testing, name = "testing")
]
