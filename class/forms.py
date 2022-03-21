from django import forms


class StudentsRegister(forms.Form):
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    career = forms.CharField(max_length=50)


class TeachersRegister(forms.Form):
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    subject_matter = forms.CharField(max_length=30)


class CareersRegister(forms.Form):
    name = forms.CharField(max_length=50)
    commission = forms.IntegerField()


class StudentsSearching(forms.Form):
    name = forms.CharField(max_length=20)



