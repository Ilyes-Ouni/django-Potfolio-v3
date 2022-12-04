from django.urls import path
from . import views

urlpatterns = [
path('infosGenerales/', views.index, name="cv"),
path('competences/', views.list_competences, name='competences'),
path('DiplomesEtFormations/', views.list_diplomesEtformations, name='DiplomesEtFormations'),
path('ExperiencesEtStages/', views.list_experiencesEtStages, name='ExperiencesEtStages'),
]

