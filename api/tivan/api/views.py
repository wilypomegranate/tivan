from rest_framework import viewsets, generics, views
from rest_framework.response import Response

from models import Camera, Event, CapturePicture, CaptureVideo
from serializers import CameraSerializer, EventSerializer, CapturePictureSerializer, CaptureVideoSerializer, CaptureVideoUpdateSerializer, EventUpdateSerializer

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

class CaptureVideoStopTimeUpdate(generics.UpdateAPIView):
    queryset = CaptureVideo.objects.all()
    serializer_class = CaptureVideoUpdateSerializer
    #lookup_field = 'path'

    def update(self, request):
        serializer = CaptureVideoUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(request.data)
            return Response(serializer.data)

class EventStopTimeUpdate(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventUpdateSerializer

    def update(self, request):
        serializer = EventUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(request.data)
            return Response(serializer.data)
