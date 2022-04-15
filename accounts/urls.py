from django import urls

from django.urls import path
from .views import login, signup, edit_user, user_detail
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", login, name = "login"),
    path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name = "logout"),
    path("signup/", signup, name = "signup"),
    path("edit_user/", edit_user, name ="edit_user"),
    path("user_detail/", user_detail, name ="user_detail"),
]
