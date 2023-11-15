from django.shortcuts import render
from news.models import Blog
from quota.models import Quota

def quota_view(request):
    quota = Quota.objects.all()
    latest_blog = Blog.objects.order_by('-id')[:3]

    context = {
        'quota':quota,
        'latest_blog': latest_blog
    }
    return render(request, 'quota.html', context)
