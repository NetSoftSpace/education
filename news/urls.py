from django.urls import path

from news.views import blog_list, blog_detail

app_name = 'news'

urlpatterns = [
    path('news/', blog_list, name='blog'),
    path('news/detail/<slug:slug>/', blog_detail, name='detail'),
]