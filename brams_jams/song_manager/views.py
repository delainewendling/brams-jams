import re
from django.shortcuts import render
from .models import Song, Tag, SongTag
from accounts.models import User
from .serializers import SongSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .helpers.authTokenHelpers import AuthTokenHelpers

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        song_title = request.data['name']
        cookies = request.META['HTTP_COOKIE']
        # user = AuthTokenHelpers.get_user_from_token(request)
        # if user is not None:
        #     song = Song.objects.create(
        #         name=song_title,
        #         user=user,
        #     )
        print("the request ", cookies)
        # user = User.object.get()
        return Response({'success'})
