from django.shortcuts import render, redirect
from Song.models import Song
from Artist.models import Artist
from Album.models import Album
from Customer.models import Customer
from django.http import Http404
from Customer.forms import UserSignupForm, CustomerLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def BasePage(request):
    return render(request, "html/base.html", {})

def HomePage(request):
    try:
        artists = Artist.objects.all()
        top = Artist.objects.order_by('followers')[:10]
        trending = Song.objects.order_by('liked')[:10]
    except Artist.DoesNotExist:
        raise Http404
    context = {
        "artist" : artists,
        "top" : top,
        "trending" : trending,
    }
    return render(request, "html/Home.html", context)

# @login_required(login_url='login/')
def ArtistPage(request, artist_name):
    try:
        artistobj = Artist.objects.get(Name=artist_name)
    except Artist.DoesNotExist:
        raise Http404
    try:
        albumsobj = Album.objects.filter(Artist=artistobj).all()
    except:
        albumsobj = None
    
    context = {
        "artist" : artistobj,
        "albums" : albumsobj,
    }
    return render(request, "html/ArtistPage.html", context)


# @login_required(login_url='login/')
def AlbumPage(request, artist_name, album_name):
    try:
        album = Album.objects.filter(Artist__Name__contains=artist_name, AlbumName=album_name).get()
    except Album.DoesNotExist:
        raise Http404
    try:
        songs = Song.objects.filter(Album__Artist__Name__contains=artist_name, Album__AlbumName=album_name).all()
    except:
        songs = None
    context = {
        "album" : album,
        "songs" : songs,
    }
    return render(request, "html/ALbumPage.html", context)


def sign_in(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'html/SigninPage.html', context)

def login(request):
    form = CustomerLoginForm()
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect.')
    context = {
        'form' : form
    }
    return render(request, 'html/loginPage.html', context)

def logout(request):
    logout(request)
    redirect('login')

def ProfilePage(request):
    # user = Customer.objects.get(Username=username)
    # context = {
    #     'user' : user,
    # }
    return render(request, 'html/ProfilePage.html', {})