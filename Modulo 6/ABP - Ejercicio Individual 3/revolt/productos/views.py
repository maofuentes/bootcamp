from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import Usuario
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})