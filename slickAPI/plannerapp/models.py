from django.db import models

# Create your models here.


class PlannerApp(models.Model):
    plan= models.CharField(max_length=200)
    generated_by = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.id)
