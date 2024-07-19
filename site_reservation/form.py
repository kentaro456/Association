from mailbox import Message
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Reservation, Utilisateur
from django.contrib.auth.forms import PasswordChangeForm

from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Utilisateur


class InscriptionForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')

    def clean_mot_de_passe(self):
        mot_de_passe = self.cleaned_data['mot_de_passe']
        try:
            validate_password(mot_de_passe)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        return mot_de_passe

    class Meta:
        model = Utilisateur
        fields = ['email', 'mot_de_passe', 'nom', 'prenom', 'numero_telephone', 'adresse']
        widgets = {
            'adresse': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'email': 'Adresse e-mail',
            'nom': 'Nom',
            'prenom': 'Prénom',
            'numero': 'Numéro de téléphone',
            'adresse': 'Adresse',
        }

# Dans votre application, créez un fichier forms.py

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom']

class EmailUpdateForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['email']

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date_reservation', 'heure_debut', 'heure_fin']
        widgets = {
            'date_reservation': forms.DateInput(attrs={'class': 'form-control datetimepicker-input', 'id': 'datetimepicker1', 'data-toggle': 'datetimepicker', 'data-target': '#datetimepicker1'}),
            'heure_debut': forms.TimeInput(attrs={'class': 'form-control datetimepicker-input', 'id': 'datetimepicker2', 'data-toggle': 'datetimepicker', 'data-target': '#datetimepicker2'}),
            'heure_fin': forms.TimeInput(attrs={'class': 'form-control datetimepicker-input', 'id': 'datetimepicker3', 'data-toggle': 'datetimepicker', 'data-target': '#datetimepicker3'}),
        }


class UpdatePasswordForm(PasswordChangeForm):
    Nouveau_mdp_1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nouveau mot de passe'}))
    Nouveau_mdp_2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmer le nouveau mot de passe'}))

    class Meta:
        model = Utilisateur
        fields = ['Nouveau_mdp_1', 'Nouveau_mdp_2']

class UpdateNameForm(forms.ModelForm):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nouveau nom'}))
    prenom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nouveau prénom'}))

    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom']

class UpdateEmailForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Nouvelle adresse email'}))

    class Meta:
        model = Utilisateur
        fields = ['email']


class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Ancien mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )
    new_password1 = forms.CharField(
        label='Nouveau mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )
    new_password2 = forms.CharField(
        label='Confirmer le nouveau mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-input'}),
    )

    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get('new_password1')
        if len(new_password1) < 8:
            raise ValidationError('Le mot de passe doit contenir au moins 8 caractères.')
        return new_password1

class UpdateNameForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom']
        labels = {
            'nom': 'Nouveau prénom',
            'prenom': 'Nouveau nom',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-input'}),
            'prenom': forms.TextInput(attrs={'class': 'form-input'}),
        }

class UpdateEmailForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['email']
        labels = {
            'email': 'Nouvelle adresse email',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        user_id = forms.IntegerField(widget=forms.HiddenInput())
        model = Message
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'email': forms.EmailInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'subject': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'}),
            'message': forms.Textarea(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline h-32'}),
        }