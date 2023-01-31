from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views import generic # make generic views w/classes
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import Pregunta,Choice

class IndexView(generic.ListView): #muestra en forma de lista
    template_name = 'encuestas/index.html'
    context_object_name = 'lista_preguntas'

    def get_queryset(self):
        '''Devuelve las últimas 5 preguntas publicadas (aquellas hechas en el pasado)'''
        return Pregunta.objects.filter(fecha_pub__lte=timezone.now()).order_by('-fecha_pub')[:5]
    
class DetallesView(generic.DetailView): 
    '''DetailView pasa el objeto completo'''
    model = Pregunta
    template_name = 'encuestas/detalle.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Pregunta.objects.filter(fecha_pub__lte=timezone.now())

class ResultadosView(generic.DetailView):
    model = Pregunta
    template_name = 'encuestas/resultados.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Pregunta.objects.filter(fecha_pub__lte=timezone.now())

def vota(request, pk):
    '''
    Página que te permite votar
    - obtiene la pregunta
    - obtiene las elecciones para esa pregunta (eleccion) mediante pOST
    - devuelve error si no existe
    - cambia los votos de esa eleccion para esa pregunta
    - te lleva a la página resultados
    '''
    pregunta = get_object_or_404(Pregunta, pk=pk)
    try:
        eleccion = pregunta.choice_set.get(pk=request.POST['eleccion'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'encuestas/detalle.html', {
            'pregunta': pregunta,
            'error_message' : "No elegiste una opción"
        })
    else:
        # cambiamos el cmapo votos de la eleccion
        eleccion.votos += 1
        eleccion.save()
    return HttpResponseRedirect(
        reverse( # transforma los parametros en una url
            'encuestas:resultados',
            args=(pregunta.id,)
        )
    )
