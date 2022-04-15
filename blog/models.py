from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=200)
    

    def __str__(self):
        return f'{self.title}'
