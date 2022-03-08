from django.db import models
from Artist.models import Artist
from Song.models import Song
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(AbstractUser):
    # Phone_Number = PhoneNumberField(unique = True, null = False, blank = False)
    Photo = models.ImageField(default="No_Profile_Pic.png", upload_to = 'images')
    Playlist = models.ManyToManyField(Song, null=True, blank=True, related_name='playlist+')
    Following = models.ManyToManyField(Artist, null=True, blank=True, related_name='following+')
    LikedSongs = models.ManyToManyField(Song, null=True, blank=True, related_name='liked+')
    IsArtist = models.BooleanField(default=False)
    Artist = models.OneToOneField(Artist, on_delete=models.CASCADE, null=True, blank=True, related_name='isArtist+')

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username' : self.username})
