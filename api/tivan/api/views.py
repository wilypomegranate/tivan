from rest_framework import viewsets, generics, views
from rest_framework.response import Response
from django.http import Http404, HttpResponse, StreamingHttpResponse

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

class EventList(views.APIView):
    def get(self, request):
        """Return a list of events with media information"""
        events = []
        for event in Event.objects.order_by('-start_time').all():
            e = {
            'id': event.id,
            'camera': event.camera.id,
            'start_time': event.start_time,
            'stop_time': event.stop_time,
            'pictures': [ cp.id for cp in CapturePicture.objects.filter(event=event).all() ]
            }
            events.append(e)
        return Response(events)

class CapturePictureRetrieval(views.APIView):
    def get_object(self, pk):
        try:
            return CapturePicture.objects.get(pk=pk)
        except CapturePicture.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        picture = self.get_object(pk)
        return HttpResponse(open(picture.path, 'rb').read(), content_type='image/jpg')

class CaptureVideoRetrieval(views.APIView):

    def get_videos(self, event):
        videos = CaptureVideo.objects.filter(event=event).all()
        print videos
        for video in videos:
            #TODO - Yield a buffer here
            yield(open(video.path, 'rb').read())

    def get(self, request, event):
        return StreamingHttpResponse(self.get_videos(event), content_type='video/ogg')
