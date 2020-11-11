"""
Models
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from groupy.client import Client

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    YEAR_CHOICES = [
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
    ]
    grad_year = models.CharField('Graduation Year',max_length=30, choices=YEAR_CHOICES, blank=True)
    major = models.CharField(max_length=50, blank=True)
    schedule = models.TextField(max_length=500, blank=True)
    student_id = models.CharField('Student ID', max_length=10, blank=True)
    groups = models.ManyToManyField('StudyGroup')
    courses = TaggableManager("Courses", "ex: CS1110, ECON1010")  

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class StudyGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50, unique=True, blank=False)
    topic_course = models.CharField(max_length=20)
    members = models.ManyToManyField(User)
    tags = TaggableManager()
    groupme_option = models.BooleanField("Create GroupMe?", default=False, blank=False)    # Does the user want to generate a group message?
    groupme_id = models.CharField(max_length=100)                       # Unique identifier provided by API
    groupme_url = models.CharField(max_length=100)                      # Unique share URL provided by API

    class Meta:
        verbose_name = 'Study Group'

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
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

