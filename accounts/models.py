from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserDetails(models.Model):
    profile_image = models.ImageField(upload_to = "profile_image" , blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(null=True)
    description = models.CharField(max_length=1000)