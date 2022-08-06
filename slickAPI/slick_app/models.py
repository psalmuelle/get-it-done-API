from django.db import models

# Create your models here.


class Todo(models.Model):
    task_title = models.CharField(max_length=400)
    