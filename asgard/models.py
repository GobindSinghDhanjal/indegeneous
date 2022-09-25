from pyexpat import model
from turtle import title
from django.db import models

class Object(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    @staticmethod
    def get_all_objects():
        return Object.objects.all()

