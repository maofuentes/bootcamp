
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required, user_passes_test
from productos.models import User

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CrearUsuario, Formulario_login, Formulario_datos


def home(request):
    return render(request, 'home.html')

def is_admin(user):
    return user.groups.filter(name='Administradores').exists()

#VISTA ADMINISTRADOR    
@user_passes_test(is_admin, login_url='home')
def listar_usuarios(request):
    usuarios = User.objects.all()
    grupos = Group.objects.all()

    if not is_admin(request.user):
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')

    return render(request, 'listar.html', {'usuarios': usuarios, 'grupos': grupos})


@user_passes_test(is_admin, login_url='home')
def panel_admin(request):
    if not is_admin(request.user):
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('home')

    return render(request, 'admin.html')

#CREAR USUARIOS
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

#LOGIN DE USUARIOS
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
                    if request.user.groups.filter(name='Administradores').exists():
                        return redirect('/panel_admin')
                    else:
                        return redirect('/home')
                else:
                    return HttpResponse("Cuenta Deshabilitada")  
        else:
            return HttpResponse("Login Incorrecto")

    else:
        form = Formulario_login()
        return render(request, "login.html", {'form':form})
    

#Salir de la cuenta

def logout_usuarios(request):
    logout(request)
    return redirect("home")

#Ingresar Datos de usuario para contacto

@login_required
def datos_usuarios(request):
    if request.method=="POST":
        form = Formulario_datos(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Formulario_datos(instance=request.user)
    return render(request, 'datos_usuarios.html', {'form': form})

"""
class DatosUsuarios(UpdateView):
    model = User
    form_class = Formulario_datos
    success_url = reverse_lazy('home')
    template_name = 'datos_usuarios.html'
"""