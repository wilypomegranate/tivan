from models import Camera
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
