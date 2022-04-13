from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from .forms import SignUp



def login(request):
    
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request,user)
                return redirect("index")
            else:
                return render(request,"index/login.html", {"login_form": login_form, "message": "La contraseña no es correcta o el usuario no existe"})
        else:
            return render(request,"index/login.html", {"login_form": login_form, "message": "Los datos introducidos no son válidos"})
    
    login_form = AuthenticationForm()
    return render(request, "index/login.html", {"login_form": login_form})


    

def signup(request):
    
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            
            return redirect("login")
        else:
            return render(request,"index/signup.html", {"form" : form, "message" : "Error al registrarse, por favor confirme que sus datos sean validos"})
    
    
    form = SignUp()
    
    return render(request,"index/signup.html", {"form" : form})