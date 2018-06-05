from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.
class ContentManager(models.Manager):
    def get_safe(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

class ActiveManager(ContentManager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(date_deleted=None)

class UserContentManager(UserManager):
    def get_safe(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def get_queryset(self):
        return super(UserContentManager, self).get_queryset().filter(date_deleted=None)

class UserGraveyardManager(UserManager):
    def get_safe(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

class User(AbstractUser):
    first_name = models.CharField(max_length=32, default=None, blank=True, null=True)
    middle_name = models.CharField(max_length=32, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=32, default=None, blank=True, null=True)
    email = models.CharField(max_length=64, default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateField(null=True, default=None)
    objects = UserContentManager()

class Song(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateField(null=True, default=None)
    user = models.ForeignKey(User, related_name="songs_added", on_delete=models.SET_NULL, null=True)
    objects = ActiveManager()
    graveyard = ContentManager()

class Tag(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateField(null=True, default=None)
    user = models.ForeignKey(User, related_name="tags_added", on_delete=models.SET_NULL, null=True)
    objects = ActiveManager()
    graveyard = ContentManager()

class SongTag(models.Model):
    tag = models.ForeignKey(Tag, related_name="song_tags", on_delete=models.CASCADE)
    song = models.ForeignKey(Song, related_name="song_tags", on_delete=models.CASCADE)
    objects = ContentManager()

