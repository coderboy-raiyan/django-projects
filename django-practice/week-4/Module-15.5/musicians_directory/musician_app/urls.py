from django.urls import path
from .views import add_musician, add_album, edit_album, edit_musician, delete_album

urlpatterns = [
    path('add-musician/', add_musician, name="add_musician"),
    path('add-album/', add_album, name="add_album"),
    path('edit-album/<int:id>', edit_album, name="edit_album"),
    path('edit-musician/<int:id>', edit_musician, name="edit_musician"),
    path('delete-album/<int:id>', delete_album, name="delete_album")
]
