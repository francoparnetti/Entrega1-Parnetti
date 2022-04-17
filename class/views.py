from unicodedata import name
from django.shortcuts import redirect, render

from .models import Students, Teachers, Careers
from .forms import StudentsRegister, TeachersRegister, CareersRegister, StudentsSearching, TeachersSearching, CareersSearching
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
def students_form(request):
    if request.method == 'POST':
        form = StudentsRegister(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            students = Students(name=data['name'], last_name=data['last_name'], career=data['career'])
            students.save()
            return redirect('students_list')

    form = StudentsRegister()
    return render(request, "class/students.html", {'form': form})

@login_required
def teachers_form(request):
    if request.method == 'POST':
        form = TeachersRegister(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            teachers = Teachers(name=data['name'], last_name=data['last_name'], subject_matter=data['subject_matter'])
            teachers.save()
            return redirect('teachers_list')

    form = TeachersRegister()
    return render(request, "class/teachers.html", {'form': form})

@login_required
def careers_form(request):
    if request.method == "POST":
        form = CareersRegister(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            careers = Careers(name = data["name"], amount_of_subjects = data["amount_of_subjects"], degree_type=data["degree_type"])
            careers.save()
            return redirect("careers_list")
    
    form = CareersRegister()
    return render(request, "class/careers.html", {'form': form})



def students_list(request):

    name_to_search = request.GET.get('name', None)

    if name_to_search is not None:
        students = Students.objects.filter(name__icontains=name_to_search)

    else:
        students = Students.objects.all()

    form = StudentsSearching()
    return render(request, "class/students_list.html", {'form': form, 'students': students})


def teachers_list(request):

    name_to_search = request.GET.get('name', None)

    if name_to_search is not None:
        teachers = Teachers.objects.filter(name__icontains=name_to_search)

    else:
        teachers = Teachers.objects.all()

    form = TeachersSearching()
    return render(request, "class/teachers_list.html", {'form': form, 'teachers': teachers})



def careers_list(request):

    name_to_search = request.GET.get('name', None)

    if name_to_search is not None:
        careers = Careers.objects.filter(name__icontains=name_to_search)

    else:
        careers = Careers.objects.all()

    form = CareersSearching()
    return render(request, "class/careers_list.html", {'form': form, 'careers': careers})




class StudentDetail(DetailView):
    model = Students
    template_name = "class/student_detail.html"
    
    
class StudentEdit(LoginRequiredMixin, UpdateView):
    model = Students
    template_name = "class/student_edit.html"
    success_url = "/class/students_list/"
    fields = ["name", "last_name", "career"]


class StudentDelete(LoginRequiredMixin, DeleteView):
    model = Students
    template_name = "class/student_delete.html"
    success_url = "/class/students_list/"
    
    

class TeacherDetail(DetailView):
    model = Teachers
    template_name = "class/teacher_detail.html"
  
    
class TeacherEdit(LoginRequiredMixin, UpdateView):
    model = Teachers
    template_name = "class/teacher_edit.html"
    success_url = "/class/teachers_list/"
    fields = ["name", "last_name", "subject_matter"]


class TeacherDelete(LoginRequiredMixin, DeleteView):
    model = Teachers
    template_name = "class/teacher_delete.html"
    success_url = "/class/teachers_list/"

    
    
class CareerDetail(DetailView):
    model = Careers
    template_name = "class/career_detail.html"
    
    
class CareerEdit(LoginRequiredMixin, UpdateView):
    model = Careers
    template_name = "class/career_edit.html"
    success_url = "/class/careers_list/"
    fields = ["name", "amount_of_subjects","degree_type"]


class CareerDelete(LoginRequiredMixin, DeleteView):
    model = Careers
    template_name = "class/career_delete.html"
    success_url = "/class/careers_list/"