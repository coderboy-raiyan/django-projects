from django.urls import path
from .views import AddMusicianView, AddAlbumView, EditAlbumView, EditMusicianView, DeleteAlbumView

urlpatterns = [
    path('add-musician/', AddMusicianView.as_view(), name="add_musician"),
    path('add-album/', AddAlbumView.as_view(), name="add_album"),
    path('edit-album/<int:id>', EditAlbumView.as_view(), name="edit_album"),
    path('edit-musician/<int:id>', EditMusicianView.as_view(), name="edit_musician"),
    path('delete-album/<int:id>', DeleteAlbumView.as_view(), name="delete_album")
]
