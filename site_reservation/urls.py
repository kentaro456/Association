from django.urls import path, include
from . import views

urlpatterns = [
    # Page d'accueil
    path('', views.index, name='index'),

    # Inscription et authentification
    path('inscription_vue', views.inscription_vue, name='inscription_vue'),  # Formulaire d'inscription
    path('user_login', views.user_login, name='user_login'),  # Formulaire de connexion
    path('logout/', views.logout, name='logout'),  # Déconnexion de l'utilisateur

    # Pages pour les utilisateurs
    path('mon-compte', views.mon_compte, name='mon_compte'),  # Page "Mon compte" pour afficher les infos de l'utilisateur
    path('visiteur', views.visiteur, name='visiteur'),  # Page pour les visiteurs (peut-être un tableau de bord ou une page de profil)

    # Pages d'administration
    path('Theadmin', views.admin, name='admin'),  # Tableau de bord de l'administrateur

    # Gestion des erreurs
    path('error', views.error, name='error'),  # Page d'erreur générique

    # Gestion des réservations
    path('prise-de-reservation/', views.s_rev, name='s_rev'),  # Page de prise de rendez-vous
    path('create-reservation/', views.create_reservation, name='create_reservation'),  # Création d'une réservation
    path('mes-réservation/', views.mes_reservations, name='mes_reservations'),  # Affichage des réservations de l'utilisateur

    # Modification des informations utilisateur
    path('modifier-mot-de-passe/', views.modify_password, name='modifier_mot_de_passe'),  # Page de modification du mot de passe
    path('modifier/', views.modifier, name='modifier'),  # Page de modification du nom
    path('modifier-email/', views.modify_email, name='modifier_email'),  # Page de modification de l'email
    
    # Mise à jour des informations utilisateur par ID
    path('utilisateur/<int:user_id>/modifier-nom/', views.update_username, name='update_username'),  # Mise à jour du nom d'utilisateur
    path('utilisateur/<int:user_id>/modifier-email/', views.update_email, name='update_email'),  # Mise à jour de l'email
    path('utilisateur/<int:user_id>/modifier-mot-de-passe/', views.update_mot_de_passe, name='update_password'),  # Mise à jour du mot de passe
    path('admin-messages/', views.admin_message, name='admin_message'),
    path('messages/', views.message_history, name='message_history'),
    path('message/', views.mess, name='message'),
    path('send-message/', views.send_message, name='send_message'),
    path('view-messages/', views.view_messages, name='view_messages'),
    path('update_user_info/', views.update_user_info, name='update_user_info'),
    path('user-liste/', views.user_liste, name='user_liste'),
    path('user-reservation/', views.admin_reservation, name='admin_reservation'),
]
