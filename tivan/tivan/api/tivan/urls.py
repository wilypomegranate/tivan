"""tivan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'camera', views.CameraViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'capture_picture', views.CapturePictureViewSet)
router.register(r'capture_video', views.CaptureVideoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^video/path/', views.CaptureVideoStopTimeUpdate.as_view()),
    url(r'^event_end/', views.EventStopTimeUpdate.as_view()),
    url(r'^events/', views.EventList.as_view()),
    url(r'^picture/retrieval/(?P<pk>[0-9]+)/', views.CapturePictureRetrieval.as_view()),
    url(r'^video/retrieval/(?P<event>[0-9]+)/', views.CaptureVideoRetrieval.as_view()),
    url(r'^video/live/(?P<pk>[0-9]+)/', views.LiveCameraStream.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
