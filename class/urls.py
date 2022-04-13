from django.urls import path

from . import views

urlpatterns = [
    path("students/", views.students_form, name="students_form"),
    path("teachers/", views.teachers_form, name="teachers_form"),
    path("careers/", views.careers_form, name = "careers_form"),
    path("students_list/", views.students_list, name="students_list"),
    path("teachers_list/", views.teachers_list, name="teachers_list"),
    path("careers_list/", views.careers_list, name="careers_list"),
    path("students/detail/<int:pk>", views.StudentDetail.as_view() , name="student_detail"),
    path("students/edit/<int:pk>", views.StudentEdit.as_view(), name="student_edit"),
    path("students/delete/<int:pk>", views.StudentDelete.as_view(), name="student_delete"),
    path("teachers/detail/<int:pk>", views.TeacherDetail.as_view() , name="teacher_detail"),
    path("teachers/edit/<int:pk>", views.TeacherEdit.as_view(), name="teacher_edit"),
    path("teachers/delete/<int:pk>", views.TeacherDelete.as_view(), name="teacher_delete"),
    path("careers/detail/<int:pk>", views.CareerDetail.as_view() , name="career_detail"),
    path("careers/edit/<int:pk>", views.CareerEdit.as_view(), name="career_edit"),
    path("careers/delete/<int:pk>", views.CareerDelete.as_view(), name="career_delete"),
]

    

