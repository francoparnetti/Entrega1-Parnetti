from django.urls import path

from .views import students_form, list_students, teachers_form, careers_form, update_student

urlpatterns = [
    path("students/", students_form, name="students_form"),
    path("teachers/", teachers_form, name="teachers"),
    path("students_list/",list_students, name="list_students"),
    path("careers/", careers_form, name = "careers"),
    path("update/student/<int:id>", update_student, name = "update")

]

    

