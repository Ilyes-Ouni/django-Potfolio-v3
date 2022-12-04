from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import UserForm
from magasin.models import Article, Categorie
from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

# ajouter import du modele Article ici 
def index(request):
 articles = Article.objects.all().values()
 categories = Categorie.objects.all().values()
 context = {
 'articles': articles, 
 'categories': categories,
 }
 return render(request, 'diplomesEtformations.html', {'data':context})

def del_art(request, id):
 article = Article.objects.get(id=id)
 article.delete()
 return HttpResponseRedirect(reverse('articles'))

def update_art(request, id):
 art = Article.objects.get(id=id)
 cat = Categorie.objects.all().values()
 template = loader.get_template('updateArticle.html')
 context = {
 'art': art,
 'cat':cat, }
 return HttpResponse(template.render(context, request))

def update_art_action(request, id):
 lib = request.POST['libelle']
 p = request.POST['prix']
 q = request.POST['qte']
 c = request.POST['categ']
 cat = Categorie.objects.get(id=c)
 article = Article.objects.get(id=id)
 article.libelle = lib
 article.prix = p
 article.qte = q
 article.categ = cat
 article.save()
 return HttpResponseRedirect(reverse('diplomesFormationsCRUD'))

def add(request):
 cat = Categorie.objects.all().values()
 template = loader.get_template('addArticle.html')
 context = {
 'cat': cat,
 }
 return HttpResponse(template.render(context, request))


def add_art(request):
 lib = request.POST['libelle']
 p = request.POST['prix']
 q = request.POST['qte']
 da = request.POST['dateAjout']
 c = request.POST['categ']
 cat = Categorie.objects.get(id=c)
 article = Article(libelle=lib, prix=p, qte=q, dateAjout=da, categ=cat)
 article.save()
 return HttpResponseRedirect(reverse('diplomesFormationsCRUD'))

# Categorie:
def del_categorie(request, id):
 categorie = Categorie.objects.get(id=id)
 categorie.delete()
 return render(request, 'categories.html',)

def list_typesFormations(request):
    categories = Categorie.objects.all().values()
    context = {
    'categories': categories,
    }
    return render(request, 'categories.html', {'data':context})


def list_users(request):
 users = User.objects.all().values()
 template = loader.get_template('users.html')
 context = {
 'users':users,
 }
 return HttpResponse(template.render(context, request))

def update_user(request, id):
 user = User.objects.get(id=id)
 print(user.password)
#  user = User.objects.filter(id=id).values()
 template = loader.get_template('updateUser.html')
 context = {
 'user': user
 }
 return HttpResponse(template.render(context, request))

def update_user_action(request, id):
 user = User.objects.get(id=id)
 print (user.password == request.POST['oldPassword'])
 if (user.password == request.POST['oldPassword']):
      print('working')
      user.email = request.POST['email']
      user.username = request.POST['username']
      user.password = request.POST['newPassword']
      user.first_name = request.POST['first_name']
      user.last_name = request.POST['last_name']
      user.save()
 return HttpResponseRedirect(reverse('users'))

def del_user(request, id):
 user = User.objects.get(id=id)
 user.delete()
 return HttpResponseRedirect(reverse('users'))

def create_compte(request):
 user_form = UserForm()
 return render(request, 'createUser.html', {'user_form' : user_form})

def create_user_action(request):
 adrEmail = request.POST['email']
 username = request.POST['login']
 password = request.POST['mot2pass']
 confirm = request.POST['confirm']
 prenom = request.POST['prenom']
 nom = request.POST['name']
 if (password==confirm):
    user = User.objects.create_user(username, adrEmail, password)
    user.first_name = prenom
    user.last_name = nom
    user.save()
    return HttpResponseRedirect(reverse('users')) 
 else:
    print ("Mot de passe et confirmation mot de passe ne sont pas identiques")
    return HttpResponseRedirect(reverse('create_compte'))


def connect (request):
 connect_form = FormConnexion ()
 return render(request, 'connexion.html', {'connect_form' : connect_form, 'error':False}) 

def signIn(request):
 username = request.POST['login']
 password = request.POST['mot2pass']
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