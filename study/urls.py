"""
URLs
"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'study'
urlpatterns = [
    path('profile', views.update_profile, name='profile'),
    path('search', login_required(views.SearchResultsView.as_view()), name='search'),
    path('groups/<int:pk>', login_required(views.GroupView.as_view()), name='group'),
    path('create-group', login_required(views.CreateGroup.as_view()), name='create-group'),
]
