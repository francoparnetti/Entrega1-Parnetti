from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to = "blog_image" , blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'