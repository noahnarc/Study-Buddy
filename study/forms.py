"""
Forms
"""

from django import forms
from django.contrib.auth.models import User
from .models import Profile, StudyGroup

from groupy.client import Client

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
    class Meta:
        model = Profile
        fields = ('bio', 'grad_year', 'major', 'student_id', 'courses')


class CustomMMCF(forms.ModelMultipleChoiceField):
    # Custom labels for the Multiple Choice field selections -- eventually change to student IDs?
    def label_from_instance(self, User):
        return "%s" % User.email

class GroupForm(forms.ModelForm):
    # Form that allows users to create a new group and select group members
    class Meta:
        model = StudyGroup
        fields = ("group_name", "topic_course", "members", "groupme_option")
    
    group_name = forms.CharField(max_length=50)
    topic_course = forms.CharField(max_length=20)
    members = CustomMMCF(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )   
    
    def save(self, commit=True):
        newgroup = super(GroupForm, self).save(commit=False)
        create = newgroup.groupme_option
        if create:
            token = "GSTVyt66iVgWWj45IVAlXv5LLegUcSuLSyRMfBgP"
            client = Client.from_token(token)
            groupme = client.groups.create(name=newgroup.group_name, share=True)
            newgroup.groupme_id = groupme.id
            newgroup.groupme_url = groupme.share_url
            success = 'GroupMe Created!'
            message = groupme.post(text=success)
            newgroup.groupme_option = False
        if commit:
            newgroup.save()
        return newgroup