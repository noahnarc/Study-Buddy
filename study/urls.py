"""
URLs
"""

from django.urls import path
from . import views

app_name = 'study'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('profile', views.update_profile, name='profile'),
    path('search', views.SearchResultsView.as_view(), name='search'),
    path('groups/<int:pk>', views.GroupView.as_view(), name='group'),
    path('groups/message/<int:pk>', views.GroupMeView.as_view(), name='group-message'),
    path('create-group', views.CreateGroup.as_view(), name='create-group'),
]
