"""
Views
"""

from django.views.generic import TemplateView, ListView, CreateView, View, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import  messages
from django.db import transaction
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, GroupForm
from .models import StudyGroup

class IndexView(View):
    template_name = 'study/base.html'

class GroupView(DetailView):
    model = StudyGroup
    template_name = 'study/group.html'

    def get_queryset(self):
        return StudyGroup.objects.all()

class GroupMeView(DetailView):
    model = StudyGroup
    template_name = 'study/group_message.html'

    def get_queryset(self):
        return StudyGroup.objects.all()

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('study:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'study/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class SearchResultsView(ListView):
    model = StudyGroup
    template_name = 'study/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = StudyGroup.objects.filter(
                Q(group_name__icontains=query) | Q(topic_course__icontains=query)
            )
        else:
            object_list = StudyGroup.objects.all()
        return object_list


class CreateGroup(CreateView):
    model = StudyGroup
    form_class = GroupForm
    template_name = 'study/create_group.html'
    success_url = 'search'