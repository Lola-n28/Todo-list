from django.db import models

# Create your models here.

class ToDo(models.Model):
    text=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    is_closed=models.BooleanField(default=False)
    is_favorite=models.BooleanField(default=False)
    

class Books(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    genre=models.CharField(max_length=50,default=0)
    price=models.IntegerField(default=0)
    author=models.CharField(max_length=100,default=0)
    year=models.DateField(default=0)