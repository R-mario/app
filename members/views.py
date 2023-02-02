from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse

from .models import Member
from .forms import SimpleForm

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
    template = loader.get_template('main_members.html')
    return HttpResponse(template.render())

def formulario(request):
    template = loader.get_template('registro.html')
    return HttpResponse(template.render())

def registro(request):
    '''
    - pagina que muestra el formulario
    - al enviar el formulario recoge la informacion 
    - la intenta guardar, si ya existe avisa al usuario
    - si no existe la guarda satisfactoriamente
    '''
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimpleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('todos'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SimpleForm()
    return render(request, 'name.html', {'form': form})

def testing(request):
    template = loader.get_template('testing.html')
    context = { 'numeros' : list(range(1,5))}
    return HttpResponse(template.render(context,request))