from django.db import models

# Create your models here.

class Artist(models.Model):
    Name = models.CharField(max_length=100)
    Photo = models.ImageField(default="No_Image.png")

    def __str__(self):
        return f'{self.Name}'