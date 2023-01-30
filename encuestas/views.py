from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Pregunta,Choice

# Create your views here.
def index(request):
    '''
    Página principal de la aplicación'''
    lista_preguntas = Pregunta.objects.order_by('-fecha_pub')
    contexto = {
        'lista_preguntas' : lista_preguntas
    }
    return render(request, 'encuestas/index.html', contexto)

def detalle(request, p_id):
    '''
    Página de detalle sobre la pregunta'''

    pregunta = get_object_or_404(Pregunta,id=p_id)
    return render(request, 'encuestas/detalle.html',
                  {'pregunta': pregunta})

def resultados(request, p_id):
    '''
    Página sobre los resultados de la elección para esa
    pregunta'''
    resultados = Pregunta.choice_set.all()
    response = "Estos son los resultados de la pregunta %s"
    return HttpResponse(response % p_id)

def vota(request, p_id):
    '''
    Página que te permite votar'''
    return HttpResponse("Vota a la pregunta %s" % p_id)