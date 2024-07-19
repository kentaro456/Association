
from django.utils import timezone  # Correct import statement
from django.db import models
from django.contrib.auth.hashers import check_password
# Create your models here.
from django.db import models
import pytz  # Importer pytz pour spécifier le fuseau horaire


class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero_telephone = models.CharField(max_length=20, blank=True, null=True)  # Champ optionnel
    adresse = models.TextField(blank=True, null=True)  # Champ optionnel
    created_at = models.DateTimeField(default=timezone.now)  # Correct usage
    is_medecin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
    def check_password(self, raw_password):
        """
        Vérifie si le mot de passe donné correspond au mot de passe de l'utilisateur.
        """
        # Comparez les mots de passe en utilisant la méthode de comparaison de Django
        return check_password(raw_password, self.password)
    
    
class Consultation(models.Model):
    TYPE_CONSULTATION = (
        ('prenatale', 'Consultation prénatale'),
        ('echographie', 'Échographie'),
        ('postnatale', 'Consultation postnatale'),
        # Ajoutez d'autres types de consultations si nécessaire
    )
    type_consultation = models.CharField(max_length=20, choices=TYPE_CONSULTATION)
    description = models.TextField()

    def __str__(self):
        return self.get_type_consultation_display()
    
class Statut(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

def get_default_statut():
    return Statut.objects.get(nom='En attente')


class Reservation(models.Model):
    STATUT_CHOICES = [
        ('PENDING', 'En attente'),
        ('CONFIRMED', 'Confirmée'),
        ('IN_PROGRESS', 'En cours'),
        ('COMPLETED', 'Complète'),
        ('CANCELLED', 'Annulée'),
        ('UNCONFIRMED', 'Non confirmée'),
        ('REJECTED', 'Refusée'),
        ('AWAITING_PAYMENT', 'En attente de paiement'),
        ('AWAITING_APPROVAL', 'En attente de validation'),
        ('EXPIRED', 'Expirée'),
    ]

    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_reservation = models.DateTimeField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, default=get_default_statut)  # Valeur par défaut
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Réservation {self.id} pour {self.utilisateur} du {self.date_reservation} de {self.heure_debut} à {self.heure_fin}"
    
    def __str__(self):
        return f"Réservation de {self.utilisateur.username} le {self.date_reservation}"
    
class Message(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def created_at_fr(self):
        return self.created_at.astimezone(pytz.timezone('Europe/Paris')).strftime('%d-%m-%Y %H:%M:%S')
    def __str__(self):
        return self.subject
