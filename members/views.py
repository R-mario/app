from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def miembro(request, id):
    miembro = Member.objects.get(id=id)
    template = loader.get_template('miembro.html')
    contexto = { 'miembro': miembro}
    return HttpResponse(template.render(contexto, request))

def todos_miembros(request):
    miembros = Member.objects.all().values()
    template = loader.get_template('todos.html')
    contexto = { 'miembros': miembros}
    return HttpResponse(template.render(contexto, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    context = { 'numeros' : list(range(1,5))}
    return HttpResponse(template.render(context,request))