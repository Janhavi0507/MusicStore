from django.db import models
from Artist.models import Artist
from Song.models import Song
from MusicStore.utils import unique_song_id_generator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Phone_Number = PhoneNumberField(unique = True, null = False, blank = False)
    Photo = models.ImageField(default="No_Profile_Pic.png")
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name} ({self.Username})'

class Following(models.Model):
    User = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Playlist(models.Model):
    User = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)