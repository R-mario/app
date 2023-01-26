from django.urls import path,include

from . import views
from creatures.views import organism_list
from members.views import main

urlpatterns = [
    path('', views.index, name='index'),
    path('miembros/', main, name ='main'),
    path('creatures/',organism_list, name = 'oL')
]