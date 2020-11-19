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
from .models import StudyGroup, Profile
from taggit.models import Tag


# Initial attempt at generating StudyBuddy homepage *NOT IN USE*
class IndexView(View):
    template_name = 'study/base.html'

# Generate the individual StudyGroup pages
class GroupView(DetailView):
    model = StudyGroup
    template_name = 'study/group.html'

    def get_queryset(self):
        return StudyGroup.objects.all()

# Initial attempt at generating GroupMe message *NOT IN USE*
class GroupMeView(DetailView):
    model = StudyGroup
    template_name = 'study/group_message.html'

    def get_queryset(self):
        return StudyGroup.objects.all()


# Update Profile that is linked to a User update
@login_required
@transaction.atomic
def update_profile(request):
    
    # Check to make sure that a 'POST' submission was recieved
    if request.method == 'POST':

        # Obtain the user and profile form submissions
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        
        # Ensure that both the user and profile forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            
            # Save both forms
            user_form.save()
            profile_form.save()

            # Create a user object from the form
            newuser = user_form.save(commit=False)
            newuser.user = request.user
            newuser.save()
            user_form.save_m2m()

            # Create a profile object from the form
            newprof = profile_form.save(commit=False)
            newprof.user = request.user
            newprof.save()
            profile_form.save_m2m()

            # Send a success message
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('study:profile')
        
        # Otherwise, generate an error message
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    # Return to a view of the user and profile forms
    return render(request, 'study/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# Return the StudyGroup search results for a specific search term 'q'
class GroupSearchResultsView(ListView):
    model = StudyGroup
    template_name = 'study/group_search_results.html'
    
    # Define the query that will be used with the search bar
    def get_queryset(self):
        query = self.request.GET.get('q')
        
        # If there is a search term, filter StudyGroups based on terms
        if query:
            object_list = StudyGroup.objects.filter(
                Q(group_name__icontains=query) | Q(topic_course__icontains=query)
            )

        # If there is no search term, return a list of all the StudyGroups
        else:
            object_list = StudyGroup.objects.all()
        return object_list


# Return the Profile search results for a specific search term 'q'
class MemberSearchResultsView(ListView):
    model = StudyGroup
    template_name = 'study/member_search_results.html'
    
    # Define the query that will be used with the search bar
    def get_queryset(self):
        query = self.request.GET.get('q')
        
        # If there is a search term, filter Profiles based on terms
        if query:
            object_list = Profile.objects.filter(
                Q(bio__icontains=query) | Q(major__icontains=query) | Q(student_id__icontains=query) | Q(courses__name__in=[query])
                 # trying to figure out how to quesry an entir list                                                                                             
            )

        # If there is no search term, return a list of all the StudyGroups
        else:
            object_list = Profile.objects.all()
        return object_list

# Use the default model for for StudyGroup creation
class CreateGroup(CreateView):
    model = StudyGroup
    form_class = GroupForm
    template_name = 'study/create_group.html'
    success_url = 'search-groups'
    

# Join a StudyGroup via button and return the new list of members
def join_group(request, pk):

    # Obtain the current user
    new_member = request.user

    # Find the group that matches the URL request
    group = StudyGroup.objects.get(id=pk)

    # Add the new member and redirect to the group page
    group.members.add(new_member)
    group.save()

    # Redirect to the StudyGroup profile page
    return redirect('study:group', pk)
