from django import forms
from . import models
from django.contrib.auth.models import User


class UpdateProfile(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['profileBio','profileEmail','profileImage']

class UpdateUser(forms.ModelForm):
    class Meta:
        model=User
        fields=['username']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=['projectName','projectImage','projectDescription','projectUrl']

class CreateProfile(forms.ModelForm):
    class Meta:
        model=models.Profile
        fields=['profileImage','profileBio','profileEmail']

