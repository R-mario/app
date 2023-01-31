from django.urls import path

from . import views

app_name = 'encuestas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='encuestas_indice'),
    path('<int:pk>/', views.DetallesView.as_view(), name = 'detalle' ),
    path('<int:pk>/resultados/', views.ResultadosView.as_view(),
         name = 'resultados'),
    path('<int:pk>/vota/', views.vota, name = 'vota')
]