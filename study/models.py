"""
Models
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    YEAR_CHOICES = [
        ('4', '2021'),
        ('3', '2022'),
        ('2', '2023'),
        ('1', '2024'),
    ]
    grad_year = models.CharField('Graduation Year',max_length=30, choices=YEAR_CHOICES, blank=True)
    major = models.CharField(max_length=50, blank=True)
    schedule = models.TextField(max_length=500, blank=True)
    student_id = models.CharField('Student ID', max_length=10, blank=True)
    groups = models.ManyToManyField('StudyGroup')

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
    group_name = models.CharField(max_length=50)
    topic_course = models.CharField(max_length=20)
    members = models.ManyToManyField(User)

    class Meta:
        verbose_name = 'Study Group'

    def __str__(self):
        return self.group_name