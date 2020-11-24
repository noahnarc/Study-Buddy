"""
Models
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from groupy.client import Client


# Custom model Profile is linked to a specific User for authentication
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    
    # Custom labels for form selection *CHANGE EACH YEAR*
    YEAR_CHOICES = [
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
    ]
    grad_year = models.CharField('Graduation Year',max_length=30, choices=YEAR_CHOICES, blank=True)
    major = models.CharField(max_length=50, blank=True)
    student_id = models.CharField('Student ID', max_length=10, blank=True)
    groups = models.ManyToManyField('StudyGroup')
    # Generate the tags and filtering options
    courses = TaggableManager("Courses", "ex: CS1110, ECON1010")  

    # Initial attempt to generate schedules *NOT IN USE*
    schedule = models.TextField(max_length=500, blank=True)        

    # Return the email as the string representation of Profile
    def __str__(self):
        return self.user.email

"""
REFERENCES
Title: Creating a User Profile page using OneToOne field with User Model
Author: Roma
Date: Oct 4, 2020
URL: https://stackoverflow.com/questions/45936087/creating-a-user-profile-page-using-onetoone-field-with-user-model
"""
# Ensures that whenever a User is created their Profile is also created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Ensures that whenever a User is saved their Profile is also saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Custom model StudyGroup has a many-to-many relationship with Users
class StudyGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50, unique=True, blank=False)
    topic_course = models.CharField(max_length=20)
    members = models.ManyToManyField(User)
    tags = TaggableManager()
    
    """
    REFERENCES
    Title: Groupy
    Author: rhgrant10
    Date: Nov 9, 2020
    URL: https://github.com/rhgrant10/Groupy
    License: Apache 2.0 License
    """
    # Attributes needed for GroupMe integration
    groupme_option = models.BooleanField("Create GroupMe?", default=False, blank=False)     # Does the user want to generate a group message?
    groupme_id = models.CharField(max_length=100)                                           # Unique identifier provided by API
    groupme_url = models.CharField(max_length=100)                                          # Unique share URL provided by API

    class Meta:
        verbose_name = 'Study Group'

    def __str__(self):
        return self.group_name

    # Custom save method used to generate external GroupMe message based on form submission
    def save(self, *args, **kwargs):
        
        # Check to see if the group needs a GroupMe
        if self.groupme_option:
            
            # Create GroupMe
            token = "GSTVyt66iVgWWj45IVAlXv5LLegUcSuLSyRMfBgP"
            client = Client.from_token(token)
            groupme = client.groups.create(name=self.group_name, share=True)
            
            # Obtain identifier and share URL
            self.groupme_id = groupme.id
            self.groupme_url = groupme.share_url
            
            # Post a message in the GroupMe
            groupme.post("Welcome to GroupMe: " + self.group_name + "!")

        super(StudyGroup, self).save(*args, **kwargs)

