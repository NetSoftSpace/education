from django.db import models


class Quota(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='quota/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
