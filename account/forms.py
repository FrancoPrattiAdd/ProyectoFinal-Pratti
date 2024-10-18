from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

# Formulario de registro
class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'avatar', 'password1', 'password2']  

# Formulario para editar el perfil
class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'avatar']  
