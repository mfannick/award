from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    profileEmail=forms.EmailField()
    # profileBio=forms.CharField()
    # profileImage=forms.ImageField()
    class Meta:
        model=User
        fields=['username','profileEmail','password1','password2']


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

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model=models.Comment
#         fields=['comment']
