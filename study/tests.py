  
from django.test import TestCase
from django.contrib.auth.models import User
from study.models import Profile, StudyGroup
from .forms import *
from django.db import IntegrityError

"""
Setup Class for Testing
"""
class Setup_Class(TestCase):
    def setupProfile(self):
        self.user = User.objects.create_user(first_name="first", last_name="last", username="username")
        profile = Profile.objects.create(user=self.user, bio="bio", grad_year="2022", major="major", student_id="id")
        return profile
    
    def setupUser(self):
        self.user = User.objects.create_user(first_name="first", last_name="last", username="username")
        return self.user

"""
Signup Form Tests
"""
class SignupFormTest(TestCase):
    # The user should be able to input a first name and last name
    def test_SignupForm_full_name(self):
        form = SignupForm(data={'first_name' : "first", 'last_name' : "last"})
        self.assertTrue(form.is_valid())

    # The user should not be able to input a first name and no last name
    def test_SignupForm_first_name(self):
        form = SignupForm(data={'first_name' : "first", 'last_name' : ""})
        self.assertFalse(form.is_valid())

    # The user should not be able to input a last name and no first name
    def test_SignupForm_last_name(self):
        form = SignupForm(data={'first_name' : "", 'last_name' : "last"})
        self.assertFalse(form.is_valid())
            
    # The user should not be able to omit their name completely
    def test_SignupForm_no_name(self):
        form = SignupForm(data={'first_name' : "", 'last_name' : ""})
        self.assertFalse(form.is_valid())

    # The user should be able to add up to 30 characters
    def test_SignupForm_valid_length(self):
        form = UserForm(data={'first_name' : "", 'last_name' : "000000000011111111112222222222"})
        self.assertTrue(form.is_valid())

    # The user should not be able to add more than 30 characters
    def test_SignupForm_invalid_length(self):
        form = UserForm(data={'first_name' : "", 'last_name' : "0000000000111111111122222222223"})
        self.assertTrue(form.is_valid())

"""
User Form Tests
"""
class UserFormTest(TestCase):
    # The user should be able to save their first and last name
    def test_UserForm_valid(self):
        form = UserForm(data={'first_name' : "newfirst", 'last_name' : "newlast"})
        self.assertTrue(form.is_valid())

    # The user should be able to remove their first and last name
    def test_UserForm_valid_remove_name(self):
        form = UserForm(data={'first_name' : "", 'last_name' : ""})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid_duplicate(self):
        fake_user = Setup_Class.setupUser(self)
        try:
            Setup_Class.setupUser(self)
        except Exception as e:
            self.assertEqual(IntegrityError, type(e))

"""
Profile Form Tests
"""
class ProfileFormTest(TestCase):

    # The user should be able to enter valid data for all the inputs
    def test_ProfileForm_valid(self):
        form = ProfileForm(data={'bio' : "bio", 'grad_year' : "2022", 'major' : "major", 'student_id' : "id", 'courses' : "cs1110"})
        self.assertTrue(form.is_valid())
   
    # The user should be able to enter multiple courses
    def test_ProfileForm_valid_courses(self):
        form = ProfileForm(data={'bio' : "bio", 'grad_year' : "2022", 'major' : "major", 'student_id' : "id", 'courses' : "cs1110, cs3240"})
        self.assertTrue(form.is_valid())
    
    # The user should be able to enter duplicate courses
    def test_ProfileForm_valid_courses_duplicate(self):
        form = ProfileForm(data={'bio' : "bio", 'grad_year' : "2022", 'major' : "major", 'student_id' : "id", 'courses' : "cs1110, cs1110"})
        self.assertTrue(form.is_valid())

    # The user should not be able to enter no data for courses
    def test_ProfileForm_invalid_courses(self):
        form = ProfileForm(data={'bio' : "bio", 'grad_year' : "2022", 'major' : "major", 'student_id' : "id", 'courses' : ""})
        self.assertFalse(form.is_valid())

    # The user should not be able to enter an invalid year
    def test_ProfileForm_invalid_year(self):
        form = ProfileForm(data={'bio' : "bio", 'grad_year' : "2007", 'major' : "major", 'student_id' : "id", 'courses' : "cs1110"})
        self.assertFalse(form.is_valid())

    # The user should not be able to submit a blank form
    def test_ProfileForm_invalid_blank(self):
        form = ProfileForm(data={'bio' : "", 'grad_year' : "", 'major' : "", 'student_id' : "", 'courses' : ""})
        self.assertFalse(form.is_valid())

"""
Group Form Tests
"""
class GroupFormTest(TestCase):
    # The user should be able to create a group with valid data
    def test_GroupForm_valid(self):
        fake_user = Setup_Class.setupUser(self)
        form = GroupForm(data={'group_name' : "groupname", 'topic_course' : "course", 'groupme_option' : True, 'members' : {fake_user}})
        self.assertTrue(form.is_valid())
    
    # The user should be able to create a group with multiple users
    def test_GroupForm_valid_duplicate(self):
        fake_user = Setup_Class.setupUser(self)
        form = GroupForm(data={'group_name' : "groupname", 'topic_course' : "course", 'groupme_option' : True, 'members' : {fake_user, fake_user}})
        self.assertTrue(form.is_valid())
    
    # The user should not be able to create a group with no name
    def test_GroupForm_invalid_name(self):
        fake_user = Setup_Class.setupUser(self)
        form = GroupForm(data={'group_name' : "", 'topic_course' : "course", 'groupme_option' : True, 'members' : {fake_user, fake_user}})
        self.assertFalse(form.is_valid())

    # The user should not be able to create a group with no topic
    def test_GroupForm_invalid_topic(self):
        fake_user = Setup_Class.setupUser(self)
        form = GroupForm(data={'group_name' : "groupname", 'topic_course' : "", 'groupme_option' : True, 'members' : {fake_user, fake_user}})
        self.assertFalse(form.is_valid())

    # The user should not be able to create a group with no members
    def test_GroupForm_invalid_member(self):
        form = GroupForm(data={'group_name' : "groupname", 'topic_course' : "course", 'groupme_option' : True, 'members' : {}})
        self.assertFalse(form.is_valid())