"""
URLs
"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'study'

# URLs with "login_required" are behind Google Login
# URLs with <int:pk> refer to specific groups
urlpatterns = [
    path('profile', views.update_profile, name='profile'),
    path('search-groups', login_required(views.GroupSearchResultsView.as_view()), name='search-groups'),
    path('search-members', login_required(views.MemberSearchResultsView.as_view()), name='search-members'),
    path('groups/<int:pk>', login_required(views.GroupView.as_view()), name='group'),
    path('join-group/<int:pk>', login_required(views.join_group), name='join-group'),
    path('create-group', login_required(views.CreateGroup.as_view()), name='create-group'),
]
