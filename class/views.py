from ast import Return
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render

from .models import Students, Teachers, Careers
from .forms import StudentForm, StudentsRegister, Teachers_form, TeachersRegister
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
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
            return redirect('ProfesorLista')

    form = TeachersRegister()
    return render(request, "class/teachers.html", {'form': form})


# def careers_form(request):
#     if request.method == "POST":
#         form = CareersRegister(request.POST)
        
#         if form.is_valid():
#             data = form.cleaned_data
#             careers = Careers(name = data["name"], commission = data["commission"])
#             careers.save()
#             return redirect("carrera_lista")
    
#     form = CareersRegister()
#     return render(request, "class/careers.html", {'form': form})

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

# def teachers_list(request):

#     list_teachers = Teachers.objects.all()
#     return render(
#         request, "class/teachers_list.html",
#         {"list_teachers": list_teachers}
# )


#crud basico
def update_teachers(request, id):

        profesores = Teachers.objects.get(id=id)

        if request.method == "POST":
            form = Teachers_form(request.POST)

            if form.is_valid():
                data = form.cleaned_data
                profesores.name=data['name']
                profesores.last_name=data['last_name']
                profesores.subject_matter=data['subject_matter']                 
                profesores.save()
                return redirect('ProfesorLista')
            
        form = Teachers_form(
            initial={
                'name': profesores.name,
                'last_name': profesores.last_name,
                'subject_matter': profesores.subject_matter
            }
        )
        return render(
        request, "class/update_teachers.html",
            {"form": form, "profesores": profesores}


    )

def delete_student(request, id):
    student_delete = Students.objects.get(id=id)
    student_delete.delete()
    return redirect("list_students")

class ProfesorLista(LoginRequiredMixin, ListView):
    model = Teachers
    template_name ='/class/teachers_list.html'

class ProfesorDetalle(DetailView):
    model = Teachers
    template_name ='class/teachers_info.html'

class CarreraLista(ListView):
    model = Careers
    template_name = 'class/carrera_lista.html'

class CarreraEditar(UpdateView):
    model = Careers
    success_url = '/class/carreras/lista'
    fields = ['name', 'commission']

class CarreraBorrar(DeleteView):
    model = Careers
    success_url = '/class/carreras/lista'

class CarreraDetalle(DetailView):
    model = Careers
    template_name = 'class/carrera_info.html'

class CrearCarrera(CreateView):
    model = Careers
    success_url = '/class/carreras/lista'
    fields = ['name', 'commission']



    



