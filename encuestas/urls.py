from django.urls import path

from . import views

app_name = 'encuestas'
urlpatterns = [
    path('', views.index, name='encuestas_indice'),
    path('<int:p_id>/', views.detalle, name = 'detalle' ),
    path('<int:p_id>/resultados/', views.resultados,
         name = 'resultados'),
    path('<int:p_id>/vota/', views.vota, name = 'votar')
]