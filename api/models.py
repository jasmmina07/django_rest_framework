from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    completed   = models.BooleanField(default=False, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.id} - {self.title}'

class User(models.Model):
    username = models.TextField()
    password = models.TextField()

    def __str__(self):
        return f"{self.id}){self.username}"