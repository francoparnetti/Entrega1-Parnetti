from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    subject_matter = models.CharField(max_length=30)

    
    def __str__(self):
        return f'{self.name} {self.last_name} {self.subject_matter}'


class Students(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    career = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name} {self.career}'
        
              
class Careers(models.Model):
    name = models.CharField(max_length=50)
    commission = models.IntegerField()

