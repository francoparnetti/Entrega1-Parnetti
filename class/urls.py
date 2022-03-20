from django.urls import path
from .views import forms, students_list

urlpatterns = [
    path("forms/", forms, name="Forms"),
    path("students",students_list, name="students_list")
]

    

