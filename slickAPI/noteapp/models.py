from django.db import models

# Create your models here.

class NoteApp(models.Model):
    title= models.CharField(max_length=100)
    note = models.TextField(max_length=1000)
    generated_by = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.id)
