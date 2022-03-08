from django.db import models
from Album.models import Album

# Create your models here.

class Song(models.Model):
    Audio_ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    Song_Audio = models.FileField(upload_to='audio', null=True)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.Title} ({self.Album.AlbumName})'
    
    def total_likes(self):
        return self.likes.count()
