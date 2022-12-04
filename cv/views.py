from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from magasin.models import Article, Categorie

# ajouter import du modele Article ici 
def index(request):
#  articles = Article.objects.all().values()
#  categories = Categorie.objects.all().values()
#  context = {
#  'articles': articles, 
#  'categories': categories,
#  }
# , {'data':context}
 return render(request, 'infosGenerales.html')

def list_competences(request):
    categories = Categorie.objects.all().values()
    context = {
    'categories': categories,
    }
    return render(request, 'competences.html', {'data':context})

def list_diplomesEtformations(request):
    categories = Categorie.objects.all().values()
    context = {
    'categories': categories,
    }
    return render(request, 'diplomesFormations.html', {'data':context})


def list_experiencesEtStages(request):
    categories = Categorie.objects.all().values()
    context = {
    'categories': categories,
    }
    return render(request, 'experiencesStages.html', {'data':context})

