from django import urls

from django.urls import path
from .views import create_blog, blog_feed

urlpatterns = [
    path("create/", create_blog, name="create_blog"),
    path("feed/", blog_feed, name="blog_feed"),
]
