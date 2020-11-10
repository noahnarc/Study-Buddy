from django.test import TestCase
from django.contrib.auth.models import User
from study.models import Profile, StudyGroup
from .forms import *

# Create your tests here.
class Setup_Class(TestCase):
    def setup(self):
        self.user = User.objects.create_user(first_name="first", last_name="last")
        studygroup = StudyGroup.objects.create(id="id", group_name="groupname", topic_course="course", members={User})
        profile = Profile.objects.create(user=self.user, bio="bio", grad_year="2022", major="major", student_id="id")
        return profile

class SignupFormTest(TestCase):
    def test_SignupForm_valid(self):
        form = SignupForm(data={'first_name' : "first", 'last_name' : "last"})
        self.assertTrue(form.is_valid())
        
    def test_SignupForm_invalid(self):
        form = SignupForm(data={'first_name' : "", 'last_name' : ""})
        self.assertFalse(form.is_valid())

class UserFormTest(TestCase):
    def test_UserForm_valid(self):
        form = UserForm(data={'first_name' : "first", 'last_name' : "last"})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = UserForm(data={'first_name' : "", 'last_name' : ""})
        self.assertFalse(form.is_valid())

class ProfileFormTest(TestCase):
    def test_ProfileForm_valid(self):
        form = ProfileForm(data={'bio' : "bio", 'grad_year' : "2022", 'major' : "major", 'student_id' : "id"})
        self.assertTrue(form.is_valid())

    def test_ProfileForm_invalid(self):
        form = ProfileForm(data={'bio' : "", 'grad_year' : "", 'major' : "", 'student_id' : ""})
        self.assertFalse(form.is_valid())

class GroupFormTest(TestCase):
    def test_GroupForm_valid(self):
        form = GroupForm(data={'group_name' : "groupname", 'topic_course' : "course"})
        self.assertTrue(form.is_valid())

