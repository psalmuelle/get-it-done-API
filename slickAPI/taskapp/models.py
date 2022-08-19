from turtle import title
from django.db import models

# Create your models here.


class TodoList(models.Model):
    list = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)



class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    deadline= models.DateField()
    todolists = models.ForeignKey(TodoList, on_delete=models.CASCADE)
