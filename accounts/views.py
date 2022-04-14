from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from .forms import SignUp, EditUser
from django.contrib.auth.decorators import login_required
from .models import UserDetails


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
                return render(request,"accounts/login.html", {"login_form": login_form, "message": "La contraseña no es correcta o el usuario no existe"})
        else:
            return render(request,"accounts/login.html", {"login_form": login_form, "message": "Los datos introducidos no son válidos"})
    
    login_form = AuthenticationForm()
    return render(request, "accounts/login.html", {"login_form": login_form})


    

def signup(request):
    
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            
            return redirect("login")
        else:
            return render(request,"accounts/signup.html", {"form" : form, "message" : "Error al registrarse, por favor confirme que sus datos sean validos"})
    
    
    form = SignUp()
    
    return render(request,"accounts/signup.html", {"form" : form})

@login_required
def edit_user(request):
    
    loged_user, _ = UserDetails.objects.get_or_create(user=request.user)
    #El get or create devuelve dos valores, uno es el que necesitamos en loged user, y el otro es un booleano. Se suele usar el "_" como segundo nombre para asignarle el booleano, porque la mayor parte de las veces no se utiliza.
    
    if request.method == "POST":
        form = EditUser(request.POST,request.FILES)
        if form.is_valid():
            request.user.email = form.cleaned_data["email"]
            request.user.first_name = form.cleaned_data["first_name"]
            request.user.last_name = form.cleaned_data["last_name"]
            loged_user.profile_image = form.cleaned_data["profile_image"]
            loged_user.link = form.cleaned_data["link"]
            loged_user.description = form.cleaned_data["description"]
            
            if form.cleaned_data["password1"] == form.cleaned_data["password2"] and form.cleaned_data["password1"] != "":
                request.user.set_password(form.cleaned_data["password1"])
            
            request.user.save()
            loged_user.save()
            
            return redirect("index")
        else:
            return render(request,"edit_user/signup.html", {"form" : form, "message" : "Error al registrarse, por favor confirme que sus datos sean validos"})
    
    
    form = EditUser(
        initial={
            "email": request.user.first_name,
            "password1": "",
            "password2": "",
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "profile_image": loged_user.profile_image,
            "description": loged_user.description,
            "link": loged_user.link,
            }
        )
    
    return render(request,"accounts/edit_user.html", {"form" : form})