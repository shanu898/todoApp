from django.db import models

# Create your models here.
class get_tasks(models.Model):
    desc=models.TextField()
    owner=models.CharField(max_length=255)
    cDate=models.DateTimeField()
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.desc} "