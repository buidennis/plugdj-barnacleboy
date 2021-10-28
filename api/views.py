from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


# View that returns all the different Rooms
# queryset, what we want
# serializer_class, how we will convert the Room to JSON
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
