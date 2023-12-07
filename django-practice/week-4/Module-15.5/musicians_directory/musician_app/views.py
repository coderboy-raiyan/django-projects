from django.shortcuts import render, redirect
from .forms import MusicianForm, AlbumForm
from .models import Album, Musician
# Create your views here.


def add_musician(request):
    if (request.method == 'POST'):
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = MusicianForm()
    return render(request, 'add_musician.html', {'form': form})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    update_musician = MusicianForm(instance=musician)

    if (request.method == 'POST'):
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, 'add_musician.html', {'form': update_musician})


def add_album(request):
    if (request.method == 'POST'):
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    update_album = AlbumForm(instance=album)

    if (request.method == 'POST'):
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, 'add_album.html', {'form': update_album})


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("home")
