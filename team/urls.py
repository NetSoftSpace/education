from django.urls import path

from team.views import team_view


app_name = 'team'

urlpatterns = [
    path('team/', team_view, name='team_view')
]


