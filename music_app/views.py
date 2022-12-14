from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from music_app.models import Artist, Song 
from music_app.forms import ArtistForm, SongForm
from django.urls import reverse_lazy


class LandingPageView(TemplateView):
    template_name = 'home.html'

class ArtistListView(ListView):
    model = Artist
    context_object_name = 'artist'
    template_name = 'list_artists.html'

class ArtistCreateView(CreateView):
    model = 'Artist'
    form_class = ArtistForm
    template_name = 'add_artist.html'
    success_url = reverse_lazy('artists')

class ArtistUpdateView(UpdateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'edit_artist.html'
    success_url = reverse_lazy('artists')


def deleteArtist(request, pk):
    artist = Artist.objects.get(id=pk)
    artist.delete()
    return redirect('/artists')




class LandingPageView(TemplateView):
    template_name = 'home.html'

class SongListView(ListView):
    model = Song
    context_object_name = 'artist'
    template_name = 'list_songs.html'

class SongCreateView(CreateView):
    model = 'Song'
    form_class = SongForm
    template_name = 'add_song.html'
    success_url = reverse_lazy('songs')

class SongUpdateView(UpdateView):
    model = Song
    form_class = SongForm
    template_name = 'edit_song.html'
    success_url = reverse_lazy('songs')


def deleteArtist(request, pk):
    song = Song.objects.get(id=pk)
    song.delete()
    return redirect('/songs')

