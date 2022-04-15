from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    body = RichTextField(blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f'{self.title}'
