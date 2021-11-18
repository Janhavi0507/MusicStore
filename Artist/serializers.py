from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artist
    fields = ['Name', 'Photo']