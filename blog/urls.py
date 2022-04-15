from django import urls

from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_blog, name="create_blog"),
    path("feed/", views.blog_feed, name="blog_feed"),
    path("<int:pk>/", views.BlogDetail.as_view(), name="blog_detail"),
    path("<int:pk>/edit/", views.BlogEdit.as_view(), name="blog_edit"),
    path("<int:pk>/delete/", views.BlogDelete.as_view(), name="blog_delete"),
]
