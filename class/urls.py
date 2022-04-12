from django.urls import path

from .views import CarreraDetalle, CarreraLista, CrearCarrera, delete_student, students_form, list_students, teachers_form, update_student, update_teachers, delete_student, ProfesorLista, ProfesorDetalle, CarreraBorrar, CarreraEditar, CarreraDetalle, CrearCarrera 

urlpatterns = [
    path("students/", students_form, name="students_form"),
    path("teachers/", teachers_form, name="teachers"),
    path("students_list/",list_students, name="list_students"),
    # path("careers/", careers_form, name = "careers"),
    path("update/student/<int:id>", update_student, name = "update"),
    path("update/teachers/<int:id>", update_teachers, name="teachers_update"),
    path("delete/student/<int:id>", delete_student, name = "delete_student"),
    path("profesores/", ProfesorLista.as_view(), name="ProfesorLista"),
    path(r"^profesores/(?P<pk>\d+)$", ProfesorDetalle.as_view(), name="profesor_detalle"),
    path("carreras/lista", CarreraLista.as_view(), name="carrera_lista"),
    path("carreras/<int:pk>/borrar/", CarreraBorrar.as_view(), name="borrar_carrera"),
    path("carreras/<int:pk>/editar/", CarreraEditar.as_view(), name="editar_carrera"),
    path("carreras/<int:pk>/", CarreraDetalle.as_view(), name="carrera_detalle"),
    path("carreras/crear/", CrearCarrera.as_view(), name="crear_carrera")


    

    




]

    

