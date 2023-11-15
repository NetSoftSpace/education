from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True, unique=True, max_length=220)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='blogs/')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class SubImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title

def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    return instance

pre_save.connect(blog_pre_save, sender=Blog)