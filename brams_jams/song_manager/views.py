from django.shortcuts import render
from .models import Song, Tag, SongTag
from .serializers import SongSerializer
from rest_framework import viewsets, permissions, status

# Create your views here.

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.AllowAny,)
