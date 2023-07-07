from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CrearUsuario

def home(request):
    return render(request, 'home.html')

def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def crear_usuarios(request):
    if request.method == "POST":
        form = CrearUsuario(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data["email"]
            user.save()
            messages.success(request, f"Usuario {user.username} creado con exito")
            return redirect("/home")
    else:
        form = CrearUsuario()
        
        context = {"form": form}
        return render(request, 'registro.html', context)