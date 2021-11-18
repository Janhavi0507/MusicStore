from django.db import models
from django.urls import reverse

# Create your models here.

class Artist(models.Model):
    Name = models.CharField(max_length=100)
    Photo = models.ImageField(default="images/No_Image.png", upload_to='images')
    followers = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f'{self.Name}'

    def get_absolute_url(self):
        return reverse("artist", kwargs={'name' : self.Name})