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
    name = forms.CharField(max_length=50, label = "Carrera")
    amount_of_subjects = forms.IntegerField(label="Cantidad de materias", min_value=0, max_value=99)
    degree_type = forms.CharField(max_length=20, label="Titulo")


class StudentsSearching(forms.Form):
    name = forms.CharField(max_length=20, label = "Buscar Estudiante")


class TeachersSearching(forms.Form):
    name = forms.CharField(max_length=20, label = "Buscar Profesor")
    
    
class CareersSearching(forms.Form):
    name = forms.CharField(max_length=20, label = "Buscar Carrera")
