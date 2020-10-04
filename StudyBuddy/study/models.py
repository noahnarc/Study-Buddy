"""
Models
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import django.contrib.auth as auth


class Profile(models.Model):
    user = models.OneToOneField(auth.get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    grad_year = models.CharField(max_length=30, blank=True)
    major = models.CharField(max_length=50, blank=True)


@receiver(post_save, sender=auth.get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=auth.get_user_model())
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
