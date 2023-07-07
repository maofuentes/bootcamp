from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CrearUsuario(UserCreationForm):
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
