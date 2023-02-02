from django.urls import path,include

from . import views
from creatures.views import organism_list
from members.views import main
from encuestas.views import IndexView

urlpatterns = [
    path('', views.index, name='index'),
    path('miembros/', main, name ='miembros'),
    path('creatures/',organism_list, name = 'criaturas'),
    path('encuestas/',IndexView.as_view(), name = 'encuestas')
]