from django.db import models
from django.db.models.signals import pre_save
from Album.models import Album
from .utils import unique_song_id_generator

# Create your models here.

class Song(models.Model):
    AudioID = models.CharField(max_length=10, primary_key=True)
    Title = models.CharField(max_length=200)
    SongAudio = models.FileField(upload_to='audio', null=True)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Title} ({self.Album.AlbumName})'

def presave_create_song_id(sender, instance, *args, **kwargs):
    if not instance.AudioID:
        instance.AudioID = unique_song_id_generator(instance)

pre_save.connect(presave_create_song_id, sender=Song)