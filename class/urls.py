from django.urls import path

from .views import students_form, students_list, teachers_form, careers_form

urlpatterns = [
    path("students/", students_form, name="students"),
    path("teachers/", teachers_form, name="teachers"),
    path("students_list/",students_list, name="students_list"),
    path("careers/", careers_form, name = "careers")
]

    

