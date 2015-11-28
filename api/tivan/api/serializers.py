from models import Camera, Event, CapturePicture, CaptureVideo
from rest_framework import serializers
from django.db import transaction


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

    @transaction.atomic
    def create(self, validated_data):
        event = Event(**validated_data)
        event.save()
        return event

class CapturePictureSerializer(serializers.ModelSerializer):
    camera = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Camera.objects.all())
    event_timestamp = serializers.DateTimeField(write_only=True)
    class Meta:
        model = CapturePicture
        read_only_fields = ('event',)

    @transaction.atomic
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
        read_only_fields = ('event',)

    @transaction.atomic
    def create(self, validated_data):
        camera = validated_data.pop('camera')
        event_timestamp = validated_data.pop('event_timestamp')
        event = Event.objects.filter(camera=camera, start_time=event_timestamp).all()[0]
        cp = CaptureVideo(event=event, **validated_data)
        cp.save()
        return cp

class CaptureVideoUpdateSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    path = serializers.CharField()

    @transaction.atomic
    def update(self, validated_data):
        instance = CaptureVideo.objects.filter(path=validated_data['path']).all()[0]
        instance.stop_time = validated_data['timestamp']
        instance.save()
        return instance

class EventUpdateSerializer(serializers.Serializer):
    event_timestamp = serializers.DateTimeField()
    camera = serializers.PrimaryKeyRelatedField(queryset=Camera.objects.all())
    timestamp = serializers.DateTimeField()

    @transaction.atomic
    def update(self, validated_data):
        instance = Event.objects.filter(start_time=validated_data['event_timestamp'], camera=validated_data['camera']).all()[0]
        instance.stop_time = validated_data['timestamp']
        instance.save()
        return instance
