from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group, User
from .models import User


class CrearUsuario(UserCreationForm):
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)
    class Meta:
        model = User
        fields = ["email", "password1", "password2", "group"]


class Formulario_login(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput)
    clave = forms.CharField(widget=forms.PasswordInput)

"""
class Formulario_datos(UserChangeForm):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    telefono = forms.CharField(max_length=15, required=True)
    direccion = forms.CharField(max_length=500, required=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'telefono', 'direccion']
"""

class Formulario_datos(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email',
            ]