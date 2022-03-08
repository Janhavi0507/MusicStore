from djongo import models
from Artist.models import Artist
from django.urls import reverse

# Create your models here.

class Album(models.Model):
    Serial_No = models.AutoField(primary_key=True)
    Album_Name = models.CharField(max_length=200)
    Album_Logo = models.ImageField(default="images/No_Image.png", upload_to='images')
    Release_Date = models.DateField()
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.AlbumName} ({self.Artist})'

    def get_absolute_url(self):
        return reverse("album", kwargs={'artist_name' : self.Artist, 'album_name' : self.AlbumName})