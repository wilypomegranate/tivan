from models import Camera, Event, CapturePicture, CaptureVideo
from rest_framework import serializers


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

class CapturePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapturePicture

class CaptureVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaptureVideo
