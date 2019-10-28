from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    userF=models.ForeignKey(User,on_delete=models.CASCADE)
    projectName=models.CharField(max_length=30)
    projectImage=models.ImageField(upload_to='projectImg/')
    projectDescription=models.TextField()
    projectUrl=models.URLField()
    projectTime=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.projectName
    @classmethod
    def searchProjects(cls,search_term):
        project = cls.objects.filter(projectName__icontains=search_term)
        return project

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profileImage=models.ImageField(default='default.jpg',upload_to='profileImg/')
    profileBio=models.TextField()
    profileEmail=models.EmailField()

    def __str__(self):
        return self.user.username