from django import urls

from django.urls import path
from .views import index, forms

urlpatterns = [
    path("", index, name = "index"),
    path("forms/", forms, name = "forms")
]
