from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Leader(models.Model):
    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leaders/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname


class Department(models.Model):
    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leaders/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname

class TeamLead(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leaders/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leaders/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
