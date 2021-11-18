from djongo import models
from Artist.models import Artist
from django.urls import reverse

# Create your models here.

class Album(models.Model):
    SerialNo = models.AutoField(primary_key=True)
    AlbumName = models.CharField(max_length=200)
    AlbumLogo = models.ImageField(default="images/No_Image.png", upload_to='images')
    ReleaseDate = models.DateField()
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.AlbumName} ({self.Artist})'

    def get_absolute_url(self):
        return reverse("album", kwargs={'artist_name' : self.Artist, 'album_name' : self.AlbumName})