from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.db.models.fields import CharField, IntegerField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=11, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


