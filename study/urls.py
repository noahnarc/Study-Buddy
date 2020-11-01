"""
URLs
"""

from django.urls import path
from . import views

app_name = 'study'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.update_profile, name='profile'),
    path('search', views.SearchResultsView.as_view(), name='search'),
    path('group', views.group, name='group'),
    path('create-group', views.CreateGroup.as_view(), name='create-group'),
]
