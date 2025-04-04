from django.db import models

# Create your models here.


class Read(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=12)


    def __str__(self):
        return self.name
    
