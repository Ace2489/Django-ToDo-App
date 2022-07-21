from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Task(models.Model):
    User = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    Completed = models.BooleanField()
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.Title
            