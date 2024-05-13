from rest_framework import serializers
from .models import Room

# RoomSerializer class is defined in the scope of serializers,
# it's necessary to transform the fields of the class Room into JSON format for API responses
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')