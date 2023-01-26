from django.db import models

# Create your models here.
class Organism(models.Model):
    scientific_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)
    kingdom = models.CharField(max_length=255)
    phylum = models.CharField(max_length=255)
    clss = models.CharField(max_length=255)
    order = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    genus = models.CharField(max_length=255)
    species = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.common_name}"
    
class Habitat(models.Model):
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    environment = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.organism}"

class Diet(models.Model):
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    diet = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.organism}"

class Behaviour(models.Model):
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    behaviour = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.organism}"

class Media(models.Model):
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    image = models.ImageField()
    video = models.FileField()

    def __str__(self):
        return f"{self.organism}"
    
class Reference(models.Model):
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.organism}"