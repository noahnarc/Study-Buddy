"""
Views
"""

from django.shortcuts import render, redirect
from django.contrib import  messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm


def index(request):
    return render(request, 'study/base.html')


# def update_profile(request, user_id):
#     user = auth.get_user_model().objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()


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
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'study/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
