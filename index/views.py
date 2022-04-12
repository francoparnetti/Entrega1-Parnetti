from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, "index/homepage.html", {})

def login_project(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                django_login(request, user)
                return render(request, "index/usuario_logueado.html", {'msj': f'Te logueaste {username} '})

            else:
                return render(request, "index/login.html", {'form': form, 'msj': 'No se autentico'})
        else:
            return render(request, "index/login.html", {'form': form, 'msj': 'Datos con formato incorrecto'})        
    else:
        form = AuthenticationForm
        return render(request, "index/login.html", {'form': form, 'msj': ''})

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'index/usuario_logueado.html', {'msj': f'Se creo el usuario {username}'})
        else:
            return render(request, "index/registrar.html", {'form': form, 'msj': ''})

    form = RegisterForm
    return render(request, "index/registrar.html", {'form': form, 'msj': ''})


