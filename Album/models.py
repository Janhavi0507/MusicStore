from djongo import models
from Artist.models import Artist

# Create your models here.

class Album(models.Model):
    SerialNo = models.AutoField(primary_key=True)
    AlbumName = models.CharField(max_length=200)
    AlbumLogo = models.ImageField(default='No_Image.png')
    ReleaseDate = models.DateField()
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.AlbumName} ({self.Artist})'