from django.shortcuts import render

from home.models import Student
from news.models import Blog

def home(request):
    students = Student.objects.all()
    latest_blog = Blog.objects.order_by('-id')[:3]

    context = {
        'students':students,
        'latest_blog':latest_blog
    }

    return render(request, 'index.html', context)

def about(request):
    latest_blog = Blog.objects.order_by('-id')[:3]

    context = {
        'latest_blog': latest_blog
    }
    return render(request, 'about.html', context)

def contact(request):
    latest_blog = Blog.objects.order_by('-id')[:3]

    context = {
        'latest_blog': latest_blog
    }
    return render(request, 'contact.html', context)