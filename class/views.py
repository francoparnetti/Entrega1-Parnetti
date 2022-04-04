from ast import Return
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render

from .models import Students, Teachers, Careers
from .forms import StudentForm, StudentsRegister, TeachersRegister, CareersRegister

# Create your views here.

def students_form(request):
    if request.method == 'POST':
        form = StudentsRegister(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            nuevo_estudiante= Students( 
                name = data['name'],
                last_name = data['last_name'],
                career = data['career'])

        nuevo_estudiante.save()
        return redirect('list_students')
           

    form = StudentsRegister()
    return render(request, "class/students.html", {'form': form})

def list_students(request):

    students_list = Students.objects.all()
    return render(
            request, "class/students_list.html",
            {"students_list": students_list}
    )



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


def careers_form(request):
    if request.method == "POST":
        form = CareersRegister(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            careers = Careers(name = data["name"], commission = data["commission"])
            careers.save()
            return redirect("index")
    
    form = CareersRegister()
    return render(request, "class/careers.html", {'form': form})

def update_student(request, id):

        estudiante = Students.objects.get(id=id)

        if request.method == "POST":
            form = StudentForm(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                estudiante.name= data['name']
                estudiante.last_name=data['last_name']
                estudiante.career=data['career']                 
                estudiante.save()
                return redirect('list_students')
            
        form = StudentForm(
            initial={
                'name': estudiante.name,
                'last_name': estudiante.last_name,
                'career': estudiante.career
            }
        )
        return render(
            request, "class/update_student.html",
            {"form": form, "estudiante": estudiante}


    )


