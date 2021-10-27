from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework import generics
from .models import Room


# Create your views here.
# endpoints here

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
