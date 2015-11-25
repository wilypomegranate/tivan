from models import Camera, Event, CapturePicture, CaptureVideo
from rest_framework import serializers


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

class CapturePictureSerializer(serializers.ModelSerializer):
    camera = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Camera.objects.all())
    event_timestamp = serializers.DateTimeField(write_only=True)
    class Meta:
        model = CapturePicture
        read_only_fields = ('event',)

    def create(self, validated_data):
        camera = validated_data.pop('camera')
        event_timestamp = validated_data.pop('event_timestamp')
        event = Event.objects.filter(camera=camera, start_time=event_timestamp).all()[0]
        cp = CapturePicture(event=event, **validated_data)
        cp.save()
        return cp

class CaptureVideoSerializer(serializers.ModelSerializer):
    camera = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Camera.objects.all())
    event_timestamp = serializers.DateTimeField(write_only=True)
    class Meta:
        model = CaptureVideo
        read_only_fields = ('event')

    def create(self, validated_data):
        camera = validated_data.pop('camera')
        event_timestamp = validated_data.pop('event_timestamp')
        event = Event.objects.filter(camera=camera, start_time=event_timestamp).all()[0]
        cp = CapturePicture(event=event, **validated_data)
        cp.save()
        return cp
