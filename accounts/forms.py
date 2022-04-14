import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
    
    email = forms.EmailField
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        helps_text = {k : "" for k in fields}
    
    
class EditUser(forms.Form):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput, required = False)
    password2 = forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput, required = False)
    first_name = forms.CharField(max_length=40, label = "Nombre")
    last_name = forms.CharField(max_length=40, label = "Apellido")
    profile_image = forms.ImageField(required=False)
    link = forms.URLField(required=False)
    description = forms.CharField(max_length=1000, required=False)