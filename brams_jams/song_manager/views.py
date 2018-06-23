from .models import Song, SongTag, Tag
from .serializers import SongSerializer, TagSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db import transaction


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            songs = Song.objects.filter(user=request.user)
            print("songs", songs)
            serializer = self.get_serializer(songs, many=True)
        except Exception as e:
            return Response({'error': 'There was an error retrieving your songs. The error was '+str(e)})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        song_title = request.data['song_title']
        tags = request.data['tags']
        user = request.user
        try:
            with transaction.atomic():
                new_song = Song.objects.create(
                    name=song_title,
                    user=user
                )
                for tag in tags:
                    existing_tag = Tag.objects.filter(
                        name=tag['text'],
                        user=user
                    )
                    if len(existing_tag) > 0:
                        existing_song_tag = SongTag.objects.filter(
                            song=new_song,
                            tag=existing_tag
                        )
                        if len(existing_song_tag) == 0:
                            SongTag.objects.create(
                                song=new_song,
                                tag=existing_tag
                            )
                    else:
                        new_tag = Tag.objects.create(
                            name=tag['text'],
                            user=user
                        )
                        SongTag.objects.create(
                            song=new_song,
                            tag=new_tag
                        )
                serializer = self.get_serializer(new_song)
        except Exception as e:
            return Response({'error': 'There was a problem saving your song' + str(e)})
        return Response(serializer.data)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            tags = Tag.objects.filter(user=request.user)
            print("songs", tags)
            serializer = self.get_serializer(tags, many=True)
        except Exception as e:
            return Response({'error': 'There was an error retrieving your tags. The error was ' + str(e)})
        return Response(serializer.data)


