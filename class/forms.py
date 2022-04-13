from django import forms


class StudentsRegister(forms.Form):
    name = forms.CharField(max_length=20, label = "Nombre")
    last_name = forms.CharField(max_length=30, label = "Apellido")
    career = forms.CharField(max_length=50, label = "Carrera")


class TeachersRegister(forms.Form):
    name = forms.CharField(max_length=20, label = "Nombre")
    last_name = forms.CharField(max_length=30, label = "Apellido")
    subject_matter = forms.CharField(max_length=30, label = "Materia impartida")


class CareersRegister(forms.Form):
    name = forms.CharField(max_length=50, label = "Curso")
    commission = forms.IntegerField(label = "Comision")


class StudentsSearching(forms.Form):
    name = forms.CharField(max_length=20, label = "Introduzca un nombre para buscar")


class TeachersSearching(forms.Form):
    name = forms.CharField(max_length=20, label = "Introduzca un nombre para buscar")
    
    
class CareersSearching(forms.Form):
    name = forms.CharField(max_length=20, label = "Introduzca una carrera para buscar")
