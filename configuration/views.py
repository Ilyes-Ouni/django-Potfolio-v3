from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import UserForm
from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from configuration.models import competences, diplomesFormations, experiencesStages, Types

# ajouter import du modele Article ici 
def diplomesFormationsCRUD(request):
 listeDiplomesFormations = diplomesFormations.objects.all().values()
 listeTypes = Types.objects.all().values()
 context = {
 'listeDiplomesFormations': listeDiplomesFormations, 
 'listeTypes': listeTypes,
 }
 return render(request, 'diplomesEtformations.html', {'data':context})

def del_diplomesFormations(request, id):
 currentDiplomesFormations = diplomesFormations.objects.get(id=id)
 currentDiplomesFormations.delete()
 return HttpResponseRedirect(reverse('diplomesFormationsCRUD'))

def update_diplomesFormations(request, id):
 currentDiplomesFormations = diplomesFormations.objects.filter(id=id).values().first()
 listTypes = Types.objects.all().values()
 context = {
 'currentDiplomesFormations': currentDiplomesFormations,
 'listTypes':listTypes, }
 return render(request, 'updateDiplomeFormation.html', {'data':context})

def update_diplomeFormation_action(request, id):
 title = request.POST['title']
 Type = request.POST['type']
 date = request.POST['date']
 currentType = Types.objects.get(id=Type)
 currentDiplomesFormations = diplomesFormations.objects.get(id=id)
 currentDiplomesFormations.Titre = title
 currentDiplomesFormations.Type = currentType
 currentDiplomesFormations.date = date
 currentDiplomesFormations.save()
 return HttpResponseRedirect(reverse('diplomesFormationsCRUD'))

def addDiplomeFormation(request):
 listeTypes = Types.objects.all().values()
 context = {
 'listeTypes': listeTypes,
 }
 return render(request, 'addDiplomeFormation.html', {'data':context})


def add_diplomeFormation_action(request):
 title = request.POST['title']
 date = request.POST['date']
 Type = request.POST['type']
 currentType = Types.objects.get(id=Type)
 newDiplomesFormations = diplomesFormations(Titre= title, Type= currentType, date= date)
 newDiplomesFormations.save()
 return HttpResponseRedirect(reverse('diplomesFormationsCRUD'))

# Categorie:
def del_Type(request, id):
 selectedType = Types.objects.get(id=id)
 selectedType.delete()
 return HttpResponseRedirect(reverse('typesFormationsCRUD'))

def addType(request):
 return render(request, 'addType.html')


def add_type_action(request):
 titre = request.POST['titre']
 newType = Types(nom = titre)
 newType.save()
 return HttpResponseRedirect(reverse('typesFormationsCRUD'))

def update_Type(request, id):
 currentType = Types.objects.get(id=id)
 context = {
 'currentID': id,
 'currentType': currentType,
 }
 return render(request, 'updateType.html', {'data':context})

def update_type_action(request, id):
 currentType = Types.objects.get(id=id)
 currentType.nom = request.POST['name']
 print(currentType)
 currentType.save()
 return HttpResponseRedirect(reverse('typesFormationsCRUD'))


def list_typesFormations(request):
   listeTypesDiplomesFormations = Types.objects.all().values()
   context = {
   'listeTypesDiplomesFormations': listeTypesDiplomesFormations,
   }
   return render(request, 'typesCRUD.html', {'data':context})

def connect (request):
 connect_form = FormConnexion ()
 return render(request, 'connexion.html', {'connect_form' : connect_form, 'error':False}) 

def signIn(request):
 username = request.POST['login']
 password = request.POST['mot_pass']
 user = authenticate(request, username=username, password=password)
 if user is not None:
    login(request, user)
    request.session['username'] = username 
    return HttpResponseRedirect(reverse('diplomesFormationsCRUD'))
 else:
    print("Login et/ou mot de passe incorrect")
    return render(request,'connexion.html', {'error':True})
    #return HttpResponseRedirect(reverse('connect'))

def signOut(request):
 logout(request) 
 return HttpResponseRedirect(reverse('connect'))