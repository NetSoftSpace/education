from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from news.models import Blog, SubImage


def blog_list(request):
    blogs = Blog.objects.order_by('-id')

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blog_list':page_obj,
        'latest_blog': blogs[:3]
    }

    return render(request, 'blog.html',context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    latest_blog = Blog.objects.order_by('-id')[:3]

    context = {
        'blog_detail':blog,
        'latest_blog': latest_blog
    }

    return render(request, 'blog-single.html', context)