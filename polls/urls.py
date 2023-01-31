from django.urls import path,include

from . import views
from creatures.views import organism_list
from members.views import main
from encuestas.views import IndexView

urlpatterns = [
    path('', views.index, name='index'),
    path('miembros/', main, name ='main'),
    path('creatures/',organism_list, name = 'creatures'),
    path('encuestas/',IndexView.as_view(), name = 'encuestas')
]