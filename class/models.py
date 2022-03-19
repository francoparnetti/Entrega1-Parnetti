from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject_matter = models.CharField(max_length=30)

class Students(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    career = models.CharField(max_length=50)

class Careers(models.Model):
    name = models.CharField(max_length=50)
    serie = models.IntegerField(max_length=10)