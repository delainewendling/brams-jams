from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'songs', views.SongViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'song_tags', views.SongTagViewSet)

urlpatterns = [url(r'^', include(router.urls))]

app_name = 'song_manager'