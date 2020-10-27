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
    path('create_group', views.create_group, name = 'create_group')
]
