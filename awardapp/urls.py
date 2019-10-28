from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^$',views.homePage,name='homePage'),
    url(r'^signUp/$',views.signUp,name='signUp'),
    url(r'^login/$', views.logIn, name='logIn'),
    url(r'^logout/$', views.logOut, name='logOut'),
    url(r'^viewProfile/$', views.viewProfile, name='viewProfile'),
    # url(r'^updateProfile/$', views.updateProfile, name='updateProfile'),
    # url(r'^createProfile/$', views.createProfile, name='createProfile'),
    url(r'^postProject/$', views.postProject, name='postProject'),
     url(r'^search/', views.searchProject, name='searchProject'),
    url(r'^projectDetails/(\d+)', views.projectDetails, name='projectDetails'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)