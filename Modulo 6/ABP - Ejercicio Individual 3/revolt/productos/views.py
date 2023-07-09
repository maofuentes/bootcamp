from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from .forms import CrearUsuario, Formulario_login

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
            selected_group = form.cleaned_data['group']
            user.save()
            user.groups.add(selected_group)
            return redirect("/login_usuarios")
    else:
        form = CrearUsuario()
        context = {"form": form}
        return render(request, 'registro.html', context)
    
def login_usuarios(request):
    if request.method=="POST":
        form = Formulario_login(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            clave = form.cleaned_data["clave"]
            loginuser = authenticate(request, username=usuario, password=clave )
            if loginuser is not None:
                if loginuser.is_active:
                    login(request, loginuser)
                    return redirect('/home')
                else:
                    return HttpResponse("Cuenta Deshabilitada")  
        else:
            return HttpResponse("Login Incorrecto")

    else:
        form = Formulario_login()
        return render(request, "login.html", {'form':form})