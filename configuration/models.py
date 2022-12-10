from django.db import models

class competences(models.Model):
    Titre = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Niveau = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Titre

class diplomesFormations(models.Model):
    Titre = models.CharField(max_length=100)
    Type =  models.ForeignKey('Types', on_delete=models.CASCADE,)
    date = models.DateField()
    def __str__(self) -> str:
        return self.Titre

class Types(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nom

class experiencesStages(models.Model):
    Titre = models.CharField(max_length=100)
    Entreprise =  models.CharField(max_length=100)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    def __str__(self) -> str:
        return self.Titre


 
 


