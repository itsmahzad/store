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


class Province(models.Model):
    province_name = models.CharField(max_length=50, null=True, blank=True)
    province_code = models.CharField(max_length=50, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.province_name


class City(models.Model):
    city_name = models.CharField(max_length=50, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities', null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.city_name


class Address(models.Model):
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address_detail = models.TextField(null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.user}'s addresses"