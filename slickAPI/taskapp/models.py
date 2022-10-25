from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    deadline= models.DateField()
  

class TodoList(models.Model):
    list = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    todo = models.ForeignKey(Todo, on_delete= models.CASCADE, null = True)




