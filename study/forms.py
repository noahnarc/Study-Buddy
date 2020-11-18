"""
Forms
"""

from django import forms
from django.contrib.auth.models import User
from .models import Profile, StudyGroup

from groupy.client import Client


# Initial signup form was designed to let users customize their names *NOT IN USE*
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    # Including placeholder labels for profile form submission
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs['placeholder'] = 'Please include a brief description of yourself! Feel free to list any specific topics where you are looking for help or feel you could help others.'
        self.fields['courses'].widget.attrs['placeholder'] = 'Ex: CS1110, CS3240, ...'

    class Meta:
        model = Profile
        # Include all the relevant fields in the profile form
        fields = ('bio', 'grad_year', 'major', 'student_id', 'courses')


class CustomMMCF(forms.ModelMultipleChoiceField):
    # Custom labels for the Multiple Choice field selections
    def label_from_instance(self, User):
        return "%s" % User.email


class GroupForm(forms.ModelForm):
    # Form that allows users to create a new group and select group members
    class Meta:
        model = StudyGroup
        fields = ("group_name", "topic_course", "members", "groupme_option")
    
    # Use the default form options
    group_name = forms.CharField(max_length=50)
    topic_course = forms.CharField(max_length=20)
    
    # Add a checkbox selection option to the form with CustomMMCF labels
    members = CustomMMCF(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )   