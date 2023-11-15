from django.shortcuts import render

from team.models import Leader, Kafedra ,Department
from news.models import Blog

def team_view(request):
    leader = Leader.objects.all()
    dep = Department.objects.all()
    kafedra = Kafedra.objects.all()
    latest_blog = Blog.objects.order_by('-id')[:3]

    context = {
        'leader':leader,
        'dep':dep,
        'kafedra':kafedra,
        'latest_blog': latest_blog
    }
    return render(request, 'team.html', context)
