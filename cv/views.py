from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from configuration.models import competences, diplomesFormations, experiencesStages, Types

# ajouter import du modele Article ici 
def index(request):
 return render(request, 'infosGenerales.html')



def list_competences(request):
    listeCompetences = competences.objects.all().values()
    context = {
    'listeCompetences': listeCompetences,
    }
    return render(request, 'competences.html', {'data':context})



def list_diplomesEtformations(request):
    listeDiplomesFormations = diplomesFormations.objects.all().values()
    listeTypes = Types.objects.all().values()
    context = {
    'listeDiplomesFormations': listeDiplomesFormations,
    'listeTypes': listeTypes,
    }
    return render(request, 'diplomesFormations.html', {'data':context})


def list_experiencesEtStages(request):
    listeExperiencesStages = experiencesStages.objects.all().values()
    context = {
    'listeExperiencesStages': listeExperiencesStages,
    }
    return render(request, 'experiencesStages.html', {'data':context})

