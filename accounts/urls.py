from django import urls

from django.urls import path
from .views import login, signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login, name = "login"),
    path("logout/", LogoutView.as_view(template_name="index/logout.html"), name = "logout"),
    path("signup/", signup, name = "signup"),
]
