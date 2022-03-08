from django.shortcuts import get_object_or_404, render, redirect
from Song.models import Song
from Artist.models import Artist
from Album.models import Album
from Customer.models import Customer
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def BasePage(request):
    return render(request, "html/base.html", {})

def HomePage(request):
    try:
        artists = Artist.objects.all()
        top = Artist.objects.order_by('followers')[:5]
        trending = Song.objects.order_by('likes')[:5]
    except Artist.DoesNotExist:
        raise Http404
    context = {
        "artist" : artists,
        "top" : top,
        "trending" : trending,
    }
    return render(request, "html/Home.html", context)

@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
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
    
    if request.method == 'POST':
        username = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # confirm password
        if len(username) > 12 or len(username) < 5:
            messages.error(request, 'Username should have length between 5 to 12 characters')
            return redirect('sign_up')
        if not username.isalnum():
            messages.error(request, 'Username should not contain special characters')
            return redirect('sign_up')
        if len(pass1) > 16 or len(pass1) < 8:
            messages.error(request, 'Password should have length between 8 to 16 characters')
            return redirect('sign_up')
        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('sign_up')

        # create user
        user = Customer.objects.create_user(username, email, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'Your account was successfully created!')
        return redirect('login')
    return render(request, 'html/SigninPage.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect(f'/Profile/{user.get_username()}/')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'html/loginPage.html')

def Logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('login')

@login_required(login_url='/login/')
def ProfilePage(request, username):
    try:
        user = Customer.objects.get(username = username)
        playlist = Customer.Playlist.all()
        following = Customer.Following.all()
    except Customer.DoesNotExist:
        user = None
        playlist = None
        following = None
    context = {
        'user' : user,
        'playlist' : playlist,
        'following' : following,
    }
    return render(request, 'html/ProfilePage.html', context)


def likeSong(request):
    song = get_object_or_404(Song, AudioID=request.POST.get('song_id'))
    if request.user in song.likes.all():
        song.likes.remove(request.user)
    else:
        song.likes.add(request.user)
    return HttpResponseRedirect(song.Album.get_absolute_url())

def UserBecomesArtist(request):
    user = request.user
    artist = Artist.objects.create(Artist_Name=user.username)