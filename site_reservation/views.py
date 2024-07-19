from collections import defaultdict
import json
from mailbox import Message
from django.shortcuts import render
from django.urls import path
from . import views
import requests
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation, Utilisateur
from .form import InscriptionForm, MessageForm, UpdateEmailForm, UpdateNameForm, UpdatePasswordForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import time
from django.contrib.auth.decorators import login_required
from .form import UserUpdateForm, EmailUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
    
from django.shortcuts import render, redirect
from .form import MessageForm
from .models import Message






# Récupérer tous les utilisateurs


# Récupérer un utilisateur spécifique par son identifiant

# Accéder aux champs de l'utilisateur

# et ainsi de suite pour d'autres champs


def index(request):
    return render(request, "../Templates/index.html")
def signup(request):
    return render(request, "../Templates/signup.html")
def s_rev(request):
    return render(request, "../Templates/create_reservation.html")

def modifier(request):
    return render(request, "../Templates/moncompte.html")
def mess(request):
    return render(request, "../Templates/message.html")

def user_admin(request):
    return render(request, "../Templates/user.html")









def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige vers la page de connexion après l'inscription réussie
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Utiliser votre fonction verif pour vérifier les informations d'identification
        user = verif(email, password)
        
        if user is not None:
            if user.is_medecin:  # Vérifier si l'utilisateur est un médecin
                # Stocker les informations de l'utilisateur dans la session
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                messages.success(request, 'Vous êtes connecté avec succès.')
                
                return redirect('admin')  # Rediriger vers la page admin après la connexion réussie
            else:
                # Stocker les informations de l'utilisateur dans la session
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email
                request.session['user_nom'] = user.nom
                request.session['user_prenom']= user.prenom 
                
                messages.success(request, 'Vous êtes connecté avec succès en tant que visiteur.')
                return redirect('visiteur')  # Rediriger vers la page visiteur après la connexion réussie
        else:
            # Authentification échouée
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            
    return render(request, 'index.html')  # Rediriger vers la page de connexion en cas de requête GET

#@login_required(login_url='/') 
def admin(request):
    return render(request, "admin.html")

def moncompte(request):
    return render(request, "moncompte.html")




def visiteur(request):
    # Vérifier si les clés existent dans la session
    user_nom = request.session.get('user_nom', None)
    user_prenom = request.session.get('user_prenom', None)
    
    # Passer les valeurs à afficher dans le contexte du template
    context = {'user_nom': user_nom, 'user_prenom': user_prenom}
    
    return render(request, "visiteur.html", context)

def error(request, email, password):
    # Passer les données d'email et de mot de passe comme contexte à la page d'erreur
    context = {'email': email, 'password': password}
    return render(request, "error.html", context)






def logout(request):
    # Déconnecter l'utilisateur en supprimant sa session
    request.session.flush()
   
    
    return redirect('index')

def verif(email, password):
    try:
        # Vérifier si un utilisateur avec cet e-mail et ce mot de passe existe dans la base de données
        utilisateurs = Utilisateur.objects.filter(email=email, mot_de_passe=password)
        if utilisateurs.exists():
            # Si au moins un utilisateur correspondant est trouvé, renvoyer le premier utilisateur
            return utilisateurs.first()
        else:
            # Si aucun utilisateur correspondant n'est trouvé, renvoyer None
            return None
    except Utilisateur.MultipleObjectsReturned:
        # Si plusieurs utilisateurs correspondent aux critères de recherche, renvoyer None ou gérer l'exception selon vos besoins
        return None



def inscription_vue(request):
    if request.method == 'POST':
        formulaire = InscriptionForm(request.POST)
        if formulaire.is_valid():
            # Enregistrer les données dans la base de données
            formulaire.save()
            # Redirection vers la page d'index après 3 secondes
            time.sleep(1.2)  # Attendre 3 secondes
            return redirect(reverse('index'))
    else:
        formulaire = InscriptionForm()
    
    return render(request, 'signup.html', {'form': formulaire})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .form import UserUpdateForm, EmailUpdateForm

def modify_password(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Votre mot de passe a été modifié avec succès.')
            return redirect('moncompte')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        password_form = PasswordChangeForm(request.user)
    return render(request, 'modify_password.html', {'password_form': password_form})

def modify_name(request):
    if request.method == 'POST':
        name_form = UserUpdateForm(request.POST, instance=request.user)
        if name_form.is_valid():
            name_form.save()
            messages.success(request, 'Votre prénom et nom ont été modifiés avec succès.')
            return redirect('moncompte')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        name_form = UserUpdateForm(instance=request.user)
    return render(request, 'modify_name.html', {'name_form': name_form})

def modify_email(request):
    if request.method == 'POST':
        email_form = EmailUpdateForm(request.POST, instance=request.user)
        if email_form.is_valid():
            email_form.save()
            messages.success(request, 'Votre adresse email a été modifiée avec succès.')
            return redirect('moncompte')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        email_form = EmailUpdateForm(instance=request.user)
    return render(request, 'modify_email.html', {'email_form': email_form})

def update_username(request, user_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')

        # Récupérer l'utilisateur à mettre à jour
        try:
            user = Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            # Gérer le cas où l'utilisateur n'est pas trouvé
            return HttpResponse("L'utilisateur n'existe pas.", status=404)
        
        # Modifier le nom et le prénom de l'utilisateur
        user.nom = nom
        user.prenom = prenom
        
        # Enregistrer les modifications dans la base de données
        user.save()
        
        # Rediriger vers une autre page ou afficher un message de succès
        return redirect('visiteur')

def update_email(request, user_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.POST.get('email')

        # Récupérer l'utilisateur à mettre à jour
        try:
            user = Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            # Gérer le cas où l'utilisateur n'est pas trouvé
            return HttpResponse("L'utilisateur n'existe pas.", status=404)
        
        # Modifier l'email de l'utilisateur
        user.email = email
        
        # Enregistrer les modifications dans la base de données
        user.save()
        
        # Rediriger vers une autre page ou afficher un message de succès
        return redirect('visiteur')

def update_mot_de_passe(request, user_id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        mot_de_passe = request.POST.get('mot_de_passe')

        # Récupérer l'utilisateur à mettre à jour
        try:
            user = Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            # Gérer le cas où l'utilisateur n'est pas trouvé
            return HttpResponse("L'utilisateur n'existe pas.", status=404)
        
        # Modifier le mot de passe de l'utilisateur
        if mot_de_passe:
            user.mot_de_passe = make_password(mot_de_passe)  # Hasher le nouveau mot de passe
        
        # Enregistrer les modifications dans la base de données
        user.save()
        
        # Rediriger vers une autre page ou afficher un message de succès
        return redirect('visiteur')
    


def create_reservation(request):
    if request.method == 'POST':
        date_reservation = request.POST.get('date_reservation')
        heure_debut = request.POST.get('heure_debut')
        heure_fin = request.POST.get('heure_fin')

        # Récupérer l'ID de l'utilisateur à partir de la session
        utilisateur_id = request.session.get('user_id')

        # Récupérer l'utilisateur à partir de son ID
        utilisateur = Utilisateur.objects.get(id=utilisateur_id)

        # Créer la réservation en utilisant les données reçues du formulaire
        reservation = Reservation(
            date_reservation=date_reservation,
            heure_debut=heure_debut,
            heure_fin=heure_fin,
            utilisateur=utilisateur,  # Utiliser l'objet Utilisateur récupéré
        )
        reservation.save()

        return redirect('mes_reservations')
    # Si la méthode de la requête n'est pas POST, afficher le formulaire vide
    return render(request, 'create_reservation.html')
from django.shortcuts import render
from .models import Reservation

def mes_reservations(request):
    # Assurez-vous que l'utilisateur est authentifié
    if 'user_id' not in request.session:
        return redirect('login')  # Redirige vers la page de connexion si l'utilisateur n'est pas authentifié
    
    # Récupérer l'ID de l'utilisateur à partir de la session
    utilisateur_id = request.session.get('user_id')
    
    # Récupérer toutes les réservations de l'utilisateur actuel
    reservations = Reservation.objects.filter(utilisateur_id=utilisateur_id)
    
    # Passer les réservations au template
    context = {
        'reservations': reservations
    }
    return render(request, 'mes_reservation.html', context)
from django.shortcuts import render, get_object_or_404

def mon_compte(request):
    
    utilisateur_id = request.session.get('user_id')  # Récupérer l'ID de l'utilisateur depuis la session
    utilisateur = get_object_or_404(Utilisateur, id=utilisateur_id)  # Récupérer l'utilisateur ou renvoyer une erreur 404 si non trouvé

    nom = utilisateur.nom
    prenom = utilisateur.prenom
    email = utilisateur.email
    adresse = utilisateur.adresse,
    numero = utilisateur.numero_telephone,



    context = {
        'utilisateur': utilisateur,
        'nom': nom,
        'prenom': prenom,
        'email': email,
        'adresse': utilisateur.adresse,
        'numero': utilisateur.numero_telephone,
        # Add other account information here if needed
    }
    return render(request, 'mon_compte.html', context)

def update_user_info(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')

        if not user_id:
            return HttpResponse("ID utilisateur manquant.", status=400)

        try:
            user = Utilisateur.objects.get(pk=user_id)
        except Utilisateur.DoesNotExist:
            return HttpResponse("L'utilisateur n'existe pas.", status=404)

        new_first_name = request.POST.get('first_name')
        new_last_name = request.POST.get('last_name')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        old_password = request.POST.get('old_password')
        new_email = request.POST.get('email')

        # Modifier le mot de passe si les champs sont remplis correctement
        if new_password1 and new_password1 == new_password2 and user.mot_de_passe == old_password:
            user.mot_de_passe = make_password(new_password1)

        # Mettre à jour le prénom et le nom
        if new_first_name:
            user.nom = new_first_name
        if new_last_name:
            user.prenom = new_last_name

        # Mettre à jour l'email
        if new_email:
            user.email = new_email

        # Enregistrer les modifications dans la base de données
        user.save()

        # Ajouter un message de succès
        messages.success(request, 'Les informations ont été mises à jour avec succès!')

        # Redirection vers une autre vue ou page
        return redirect('visiteur')

    else:
        return HttpResponse("Méthode non autorisée.", status=405)


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Récupérer l'ID de l'utilisateur actuel depuis la session
            user_id = request.session.get('user_id')
            
            # Créer une instance de Message mais ne pas enregistrer encore en base de données
            message = form.save(commit=False)
            message.user_id = user_id  # Affecter l'ID de l'utilisateur au champ user_id du message
            message.save()  # Maintenant, enregistrer le message en base de données

            return redirect('message')  # Redirection vers une page de succès après l'envoi du message

    else:
        form = MessageForm(initial={'user_id': request.user.id})  # Initialiser le formulaire avec user_id

    context = {
        'form': form,
    }
    return render(request, 'message.html', context)


def view_messages(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'admin-message.html', {'messages': messages})

def message_history(request):
    user_id = request.session.get('user_id')
    user_messages = Message.objects.filter(user_id=user_id)
    return render(request, 'message_history.html', {'user_messages': user_messages})


def admin_message(request):
   # afficher tout les message des utilisateures 
    user_messages = Message.objects.all()
    return render(request, 'admin-message.html', {'user_messages': user_messages})

def admin_reservation(request):
   # afficher tout les message des utilisateures 
    user_reservation = Reservation.objects.all()
    return render(request, 'admin-reservation.html', {'user_reservation': user_reservation})

def user_liste(request):
   # afficher tout les message des utilisateures 
    users = Utilisateur.objects.all()
    total_users = users.count()
     # Préparer les données pour le graphique
    users_by_month = defaultdict(int)
    for user in users:
        month = user.created_at.strftime('%B %Y')
        users_by_month[month] += 1
    
    context = {
        'users': users,
        'total_users': json.dumps(total_users),
        'users_by_month': json.dumps(users_by_month)
    }
    return render(request, 'user.html', context)
