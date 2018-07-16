from .models import Song, SongTag, Tag
from .serializers import SongSerializer, TagSerializer, SongTagSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db import transaction
from datetime import datetime


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            songs = Song.objects.filter(user=request.user)
            serializer = self.get_serializer(songs, many=True)
        except Exception as e:
            return Response({'error': 'There was an error retrieving your songs. The error was '+str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            song_title = request.data['song_title']
            tags = request.data['tags']
            user = request.user
            with transaction.atomic():
                new_song = Song.objects.create(
                    name=song_title,
                    user=user
                )
                for tag in tags:
                    normalized_tag = tag.title()
                    existing_tag = Tag.objects.filter(
                        name=normalized_tag,
                        user=user
                    )
                    if len(existing_tag) > 0:
                        existing_song_tag = SongTag.objects.filter(
                            song=new_song,
                            tag=existing_tag.first()
                        )
                        if len(existing_song_tag) == 0:
                            SongTag.objects.create(
                                song=new_song,
                                tag=existing_tag.first()
                            )
                    else:
                        new_tag = Tag.objects.create(
                            name=normalized_tag,
                            user=user
                        )
                        SongTag.objects.create(
                            song=new_song,
                            tag=new_tag
                        )
                serializer = self.get_serializer(new_song)
        except Exception as e:
            return Response({'error': 'There was a problem saving your song ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        try:
            song_id = kwargs['pk']
            add_tag = request.data['add']
            tag_name = request.data['tag_name']
            song = Song.objects.get(pk=song_id)
            if add_tag:
                tags = Tag.objects.filter(name=tag_name)
                if len(tags) > 0:
                    tag = tags.first()
                else:
                    tag = Tag.objects.create(name=tag_name)
                song_tag = SongTag.objects.create(
                    song=song,
                    tag=tag
                )
                song.song_tags.add(song_tag)
            else:
                tag = Tag.objects.filter(name=tag_name)
                song_tag = SongTag.objects.filter(
                    song=song,
                    tag=tag.first()
                )
                song_tag.delete()
            serializer = self.get_serializer(song)
        except Exception as e:
            return Response({'error': 'There was a problem updating the song tags ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        song_id = kwargs['pk']
        print("this is the song id ", song_id)
        try:
            song = Song.objects.filter(pk=song_id)
            song.date_deleted = datetime.now()
            song.save()
            serializer = self.get_serializer(song)
        except Exception as e:
            return Response({'error': 'There was a problem deleting your song' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        try:
            tags = Tag.objects.filter(user=request.user)
            serializer = self.get_serializer(tags, many=True)
        except Exception as e:
            return Response({'error': 'There was an error retrieving your tags. The error was ' + str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)


class SongTagViewSet(viewsets.ModelViewSet):
    queryset = SongTag.objects.all()
    serializer_class = SongTagSerializer
    permission_classes = (permissions.IsAuthenticated,)




