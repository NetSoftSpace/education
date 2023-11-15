from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='students/')
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

