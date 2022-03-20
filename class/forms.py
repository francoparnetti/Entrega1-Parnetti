


from django import forms

class StudentsFormulario(forms.Form):
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    career = forms.CharField(max_length=50)

class StudentsSearching(forms.Form):
    name = forms.CharField(max_length=20)

class TeachersFormulario(forms.Form):
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    subject_matter = forms.CharField(max_length=30)


    
