from django import urls

from django.urls import path
from .views import index, login_project, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", index, name = "index"),
    path("login/", login_project, name="login"),
    path("registrar/", register, name="registrar"),
    path("logout/", LogoutView.as_view(template_name='index/logout.html'), name="logout")

]
