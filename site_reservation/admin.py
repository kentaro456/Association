from django.contrib import admin
from .models import Utilisateur, Consultation, Reservation

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nom', 'prenom', 'is_medecin')
    list_filter = ('is_medecin',)
    search_fields = ('email', 'nom', 'prenom')

# Enregistrement des modèles avec leurs classes d'administration personnalisées
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Consultation)
admin.site.register(Reservation)
