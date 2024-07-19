# decorators.py

from django.shortcuts import redirect
from django.urls import reverse

def anonymous_required(view_func):
    def wrapper(request, *args, **kwargs):
        # Si l'utilisateur est connecté, le rediriger vers la page d'accueil ou une autre vue
        if request.user.is_authenticated:
            return redirect(reverse('home'))  # Remplacez 'home' par le nom de votre vue d'accueil

        # Sinon, permettre l'accès à la vue demandée
        return view_func(request, *args, **kwargs)

    return wrapper
