from django.urls import path
from . import views

urlpatterns = [
path('diplomesFormationsCRUD/', views.diplomesFormationsCRUD, name="diplomesFormationsCRUD"),

path('diplomesFormationsCRUD/del_diplomesFormations/<int:id>', views.del_diplomesFormations),
path('diplomesFormationsCRUD/update_diplomesFormations/<int:id>', views.update_diplomesFormations),
path('diplomesFormationsCRUD/update_diplomesFormations/update_diplomeFormation_action/<int:id>', views.update_diplomeFormation_action, name='update_art_action'),
path('diplomesFormationsCRUD/addDiplomeFormation/', views.addDiplomeFormation, name='add'),
path('diplomesFormationsCRUD/addDiplomeFormation/add_action_diplomesFormations/', views.add_diplomeFormation_action),

path('typesFormations/', views.list_typesFormations, name='typesFormationsCRUD'),
path('typesFormations/addType/', views.addType),
path('typesFormations/addType/add_type_action/', views.add_type_action),
path('typesFormations/del_Type/<int:id>', views.del_Type),
path('typesFormations/update_Type/<int:id>', views.update_Type),
path('typesFormations/update_Type/update_type_action/<int:id>', views.update_type_action),

path('', views.connect, name='connect'),
path('login/', views.signIn, name='signIn'),
path('login/login/', views.signIn, name='signIn'),
path('disconnect/', views.signOut, name='disconnect'),

]

