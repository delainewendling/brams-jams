from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.


class UserContentManager(UserManager):
    def get_safe(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def get_queryset(self):
        return super(UserContentManager, self).get_queryset().filter(active=True)


class UserGraveyardManager(UserManager):
    def get_safe(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None

class User(AbstractUser):
    first_name = models.CharField(max_length=32, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=32, default=None, blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateField(null=True, default=None)
    objects = UserContentManager()
