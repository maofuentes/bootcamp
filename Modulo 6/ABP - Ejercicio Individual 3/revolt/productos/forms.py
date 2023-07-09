from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

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
