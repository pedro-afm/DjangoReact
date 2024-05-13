from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
# Create your views here.


# RoomView will provide a list view of a queryset
class RoomView(generics.ListAPIView):
    # Fetches all instances of the Room model from the database
    # The returned data will be serialized
    queryset = Room.objects.all()
    # This will serialize the data returned
    serializer_class = RoomSerializer