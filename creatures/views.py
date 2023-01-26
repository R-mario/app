from django.shortcuts import render
from .models import Organism, Habitat, Diet, Behaviour, Media, Reference

def organism_list(request):
    organisms = Organism.objects.all()
    context = {'organisms': organisms}
    return render(request, 'creatura.html', context)

def organism_detail(request, organism_id):
    organism = Organism.objects.get(id=organism_id)
    habitat = Habitat.objects.get(organism_id=organism_id)
    diet = Diet.objects.get(organism_id=organism_id)
    behavior = Behaviour.objects.get(organism_id=organism_id)
    media = Media.objects.get(organism_id=organism_id)
    reference = Reference.objects.filter(organism_id=organism_id)
    context = {'organism': organism, 'habitat': habitat, 'diet': diet, 'behaviour': behaviour, 'media': media, 'reference': reference}
    return render(request, 'organism_detail.html', context)
