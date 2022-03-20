from unicodedata import name
from django.shortcuts import redirect, render

from .models import Students, Teachers
from .forms import StudentsRegister, StudentsSearching, TeachersRegister

# Create your views here.

def students_form(request):
    if request.method == 'POST':
        form = StudentsRegister(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            students = Students(name=data['name'], last_name=data['last_name'], career=data['career'])
            students.save()
            return redirect('index')

    form = StudentsRegister()
    return render(request, "class/students.html", {'form': form})

def students_list(request):

    name_to_search = request.GET.get('name', None)

    if name_to_search is not None:
        students = Students.objects.filter(name__icontains=name_to_search)

    else:
        students = Students.objects.all()

    form = StudentsSearching()
    return render(request, "class/students_list.html", {'form': form, 'students': students})


def teachers_form(request):
    if request.method == 'POST':
        form = TeachersRegister(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            teachers = Teachers(name=data['name'], last_name=data['last_name'], subject_matter=data['subject_matter'])
            teachers.save()
            return redirect('index')

    form = TeachersRegister()
    return render(request, "class/teachers.html", {'form': form})


