from django.contrib import admin
from configuration.models import competences, diplomesFormations, Types, experiencesStages
    
class TypeAdmin(admin.ModelAdmin):
    list_display = ('nom')
    list_filter = ('nom','id')
    search_fields = ('nom') 
    def categ_link(self, Type):
        return mark_safe('<a href="{}">{}</a>'.format(reverse("admin:infosGenerales__change", args=(diplomesFormations.Type.pk,)),diplomesFormations.Type.nom))

admin.site.register(competences)
admin.site.register(diplomesFormations)
admin.site.register(experiencesStages)
admin.site.register(Types)