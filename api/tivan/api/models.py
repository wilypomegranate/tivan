from django.db import models

class Camera(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField(default='')
    stream_url = models.CharField(max_length=255)

class Event(models.Model):
    camera = models.ForeignKey('Camera')
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(null=True)
    changed_pixels = models.IntegerField()
    noise_level = models.IntegerField()
    motion_area_width = models.IntegerField()
    motion_area_height = models.IntegerField()
    motion_center_x = models.IntegerField()
    motion_center_y = models.IntegerField()

    class Meta:
        unique_together = ('camera', 'start_time',)

class CapturePicture(models.Model):
    path = models.TextField()
    timestamp = models.DateTimeField()
    event = models.ForeignKey('Event')

class CaptureVideo(models.Model):
    path = models.TextField()
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(null=True)
    event = models.ForeignKey('Event')
