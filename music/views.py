from django.shortcuts import render
from . import models
# Create your views here.

def showsongs(request):
    songs = models.Song.objects.all()
    return render(request, 'music/songs.html', {'songs': songs})

def song_detail(request, song_id):
    song = models.Song.objects.get(pk=song_id)
    return render(request, 'music/song_detail.html', {'song': song})

def song_edit(request, song_id):
    if str(song_id) == '0':
        return render(request, 'music/song_edit.html')
    song = models.Song.objects.get(pk=song_id)
    return render(request, 'music/song_edit.html', {'song': song})

def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    artist = request.POST.get('artist', 'ARTIST')
    song_id = request.POST.get('song_id', '0')

    if song_id == '0':
        models.Song.objects.create(title=title, artist=artist)
        songs = models.Song.objects.all()
        return render(request, 'music/songs.html', {'songs': songs})
    
    song = models.Song.objects.get(pk=song_id)
    song.title = title
    song.artist = artist
    song.save()
    return render(request, 'music/song_detail.html', {'song': song})