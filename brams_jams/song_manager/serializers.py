from rest_framework import serializers
from .models import Song, Tag, SongTag

class UserNameSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.first_name + " " + instance.last_name
        }

class ItemNameSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name
        }

class SongTagSerializer(serializers.ModelSerializer):
    song = ItemNameSerializer()
    tag = ItemNameSerializer()

    class Meta:
        model = SongTag
        fields = ('id', 'tag', 'song')

class SongSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    song_tags = SongTagSerializer(many=True)

    class Meta:
        model = Song
        fields = ('id', 'name', 'date_created', 'user', 'song_tags')

class TagSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'date_created', 'user')
