from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
  

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user',
        ]


class UsernameChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', ]

