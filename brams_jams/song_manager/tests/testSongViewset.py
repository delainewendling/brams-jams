from django.test import TestCase
from model_mommy import mommy
from song_manager.models import Song
from rest_framework.test import APIClient

class TestGradeDataExport(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = mommy.make('song_manager.User', date_deleted=None)

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def testCreateSong(self):
        data = {
            "name": "Test Song",
        }
        self.client.post("/song-manager/songs", data)
        songs = Song.objects.all()
        song = songs[1]
        self.assertEqual(song.name, data['name'])
        self.assertEqual(song.user, self.user)
        self.assertIsNotNone(song.date_created)
        self.assertIsNone(song.date_deleted)


