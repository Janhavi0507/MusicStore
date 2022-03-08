"""MusicStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
# from .views import *
app_name = 'music'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    # path('', BasePage, name='base'),
    # path('Home/', HomePage, name='home'),
    # path('signup/', sign_in, name='sign_up'),
    # path('login/', Login, name='login'),
    # path('logout/', Logout, name='logout'),
    # path('like/', likeSong, name='like_song'),
    # path('Profile/<str:username>/', ProfilePage, name='profile'),
    # path('<str:artist_name>/', ArtistPage, name='artist'),
    # path('<str:artist_name>/<str:album_name>/', AlbumPage, name='album'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

