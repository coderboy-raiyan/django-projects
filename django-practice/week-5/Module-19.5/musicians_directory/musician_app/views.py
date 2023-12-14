from django.shortcuts import render, redirect
from .forms import MusicianForm, AlbumForm
from .models import Album, Musician
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.


@method_decorator(login_required, name="dispatch")
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = "add_musician.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Musician created Successfully")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "add_album.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Album created Successfully")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'add_album.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Album updated Successfully")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    pk_url_kwarg = 'id'
    template_name = 'add_musician.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Musician updated Successfully")
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class DeleteAlbumView(DeleteView):
    model = Album
    pk_url_kwarg = 'id'
    template_name = 'delete_album.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        messages.success(self.request, "Album Deleted Successfully")
        return super().form_valid(form)


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
