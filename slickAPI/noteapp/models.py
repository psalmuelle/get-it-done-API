from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NoteApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title= models.CharField(max_length=100)
    note = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.id)
