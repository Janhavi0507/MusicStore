from django.shortcuts import render
from .models import Artist
from Album.models import Album
from django.http import Http404

# Create your views here.

def ArtistPage(request, name):
    try:
        object = Artist.objects.get(Name=name)
    except Artist.DoesNotExist:
        raise Http404
    try:
        albums = [Album.objects.get(Artist=object)]
    except:
        albums = None
    context = {
        "obj" : object,
        "albums" : albums,
    }
    return render(request, "ArtistPage.html", context)

def HomePage(request):
    try:
        object = Artist.objects.all()
    except Artist.DoesNotExist:
        raise Http404
    context = {
        "obj" : object,
    }
    return render(request, "Home.html", context)