from django.contrib import admin
from magasin.models import Article
from magasin.models import Categorie

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'categ', 'prix', 'qte')
    list_filter = ('libelle', 'prix')
    date_hierarchy = 'dateAjout'
    ordering = ('dateAjout',)
    search_fields = ('libelle', 'categ')
    
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nomCat', 'apercu')
    # list
    list_filter = ('nomCat','id')
    #filtrage à droit 
    search_fields = ('libelle', 'qte') 
    def apercu (self, categ):
        text = categ.description[:40]
        if len(categ.description) > 40:
            return '{}...'.format(text)
        else:
            return text
    def categ_link(self, art):
        return mark_safe('<a href="{}">{}</a>'.format(reverse("admin:magasin_categorie_change", args=(art.categ.pk,)),art.categ.nomCat))


admin.site.register(Article, ArticleAdmin)
#----> l'affichage de table Article selon les critères de classe ArticleAdmin
admin.site.register(Categorie, CategorieAdmin)