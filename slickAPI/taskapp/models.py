from django.db import models

# Create your models here.



class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    generated_by = models.IntegerField()
    deadline= models.DateField()



class TodoList(models.Model):
    list = models.TextField(max_length=100)
    completed = models.BooleanField(default=False)
    todo_id = models.IntegerField()

