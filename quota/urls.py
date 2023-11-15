from django.urls import path

from quota.views import quota_view


app_name = 'quota'

urlpatterns = [
    path('quota/', quota_view, name='quota_view')
]