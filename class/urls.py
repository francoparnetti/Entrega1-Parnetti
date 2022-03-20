from django.urls import path

from .views import forms, students_list,TeachersForms

urlpatterns = [
    path("forms/", forms, name="Forms"),
    path("Teachers/",TeachersForms, name="teachers"),
    path("students/",students_list, name="students_list")
]

    

