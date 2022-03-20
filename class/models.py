from django.db import models

class Teachers(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    subject_matter = models.CharField(max_length=30)


class Students(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    career = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'
        
class Careers(models.Model):
    name = models.CharField(max_length=50)
    serie = models.IntegerField()

