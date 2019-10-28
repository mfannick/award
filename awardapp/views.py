from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfile,UpdateUser,ProjectForm,CreateProfile
from .models import Profile,Project
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# "token": "f32dbfb4e7b32dd468268991c1872a91d50f6891"

#serializing

############# project model

class ProjectList(APIView):
    def get(self, request, format=None):
        allProjects = Project.objects.all()
        serializers = ProjectSerializer(allProjects, many=True)
        return Response(serializers.data)

        def post(self, request, format=None):
            serializers = ProjectSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            permission_classes = (IsAdminOrReadOnly,)



class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_merch(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_merch(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        project = self.get_merch(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############# profile model

class ProfileList(APIView):
    def get(self, request, format=None):
        allProfiles = Profile.objects.all()
        serializers = ProfileSerializer(allProfiles, many=True)
        return Response(serializers.data)

        def post(self, request, format=None):
            serializers = ProfileSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
            permission_classes = (IsAdminOrReadOnly,)



class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_merch(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_merch(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        profile = self.get_merch(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# Create your views here.
def homePage(request):
    projects=Project.objects.all()
    return render(request,'project/homePage.html',{'projects':projects})

def signUp(request):
    currentUser=request.user
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'{username} , your account was successfuly created')
            return redirect('logIn')
    else:
        form=UserCreationForm()
    return render(request,'auth/signUp.html',{'form':form})

def logIn(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homePage')
    else:
        form=AuthenticationForm()
    return render(request,'auth/logIn.html',{'form':form})

def logOut(request):
    if request.method=='POST':
        logout(request)
        return redirect('homePage')

def viewProfile(request):
    profiles=Profile.profileEmail
    if request.method=='POST':
        currentUser=request.user
        profile=request.user
        userForm=UpdateUser(request.POST,instance=request.user)
        profileForm=UpdateProfile(request.POST,instance=profile)
       

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            
            messages.success(request,f' your account has been updated successfuly ')
            return redirect('viewProfile')
    else: 
        userForm=UpdateUser(instance=request.user)
        profileForm=UpdateProfile(instance=request.user)
        

    return render(request,'auth/profile.html',{'uform':userForm,'pform':profileForm,'profiles':profiles})
# @login_required(login_url='/login/')
# def viewProfile(request):
#     if request.method=='POST':
        
        
#         userForm=UpdateUser(request.POST,instance=request.user)
        
#         # imageUpdate=UpdateProfileImage(request.POST,request.FILES,instance=profileImage)

#         if userForm.is_valid():
#             userForm.save()
           
#             messages.success(request,f' your account has been updated successfuly ')
#             return redirect('viewProfile')
#     else:
      
#         # profileImage=request.user.profile.profileImage
#         userForm=UpdateUser(instance=request.user)
        
#         # imageUpdate=UpdateProfileImage(instance=request.user.profile.profileImage)
#         # ,'iform':imageUpdate
        

#     return render(request,'auth/profile.html',{'uform':userForm})



# def updateProfile(request):
#     current_user = request.user
#     if request.method=='POST':
#         form=UpdateProfile(request.POST,request.FILES)
#         if form.is_valid():
#             profiles=form.save()
#             profiles==Profile
            
            

#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('viewProfile' )
#     else:
#         form=UpdateProfile()
#     return render(request,'auth/profileUpdate.html',{'form':form})


# def createProfile(request):
#     current_user = request.user
#     if request.method=='POST':
#         form=CreateProfile(request.POST,request.FILES)
#         if form.is_valid():
#             profile=form.save(commit=False)
#             profile.userF=current_user
#             profile.save()

#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#             else:
#                 return redirect('viewProfile' )
#     else:
#         form=CreateProfile()
#     return render(request,'auth/createProfile.html',{'form':form})

@login_required(login_url='/login/')
def postProject(request):
    current_user = request.user
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.userF=current_user
            project.save()

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homePage' )
    else:
        form=ProjectForm()
    return render(request,'project/postProject.html',{'form':form})



def projectDetails(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"project/projectDetails.html", {'project':project})
        
            



