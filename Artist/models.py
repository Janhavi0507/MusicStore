from django.db import models
from django.urls import reverse

# Create your models here.

class Artist(models.Model):
    Artist_Id = models.BigAutoField(primary_key=True)
    Artist_Name = models.CharField(max_length=100)
    Photo = models.ImageField(default="images/No_Image.png", upload_to='images')
    Followers = models.PositiveBigIntegerField(default=0)
    # Date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.Name}'

    def get_absolute_url(self):
        return reverse("artist", kwargs={'name' : self.Name})