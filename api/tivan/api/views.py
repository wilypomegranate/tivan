from rest_framework import viewsets

from models import Camera, Event, CapturePicture, CaptureVideo
from serializers import CameraSerializer, EventSerializer, CapturePictureSerializer, CaptureVideoSerializer

class CameraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cameras to be viewed or edited.
    """
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CapturePictureViewSet(viewsets.ModelViewSet):
    queryset = CapturePicture.objects.all()
    serializer_class = CapturePictureSerializer

class CaptureVideoViewSet(viewsets.ModelViewSet):
    queryset = CaptureVideo.objects.all()
    serializer_class = CaptureVideoSerializer
