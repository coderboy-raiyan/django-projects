from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    # path('add/', views.add_posts, name="add_posts"),
    # path('edit/<int:id>', views.edit_posts, name="edit_posts"),
    # path('delete/<int:id>', views.delete_posts, name="delete_posts"),
    path('add/', views.AddPostCreateView.as_view(), name="add_posts"),
    path('edit/<int:id>', views.EditPostView.as_view(), name="edit_posts"),
    path('delete/<int:id>', views.DeletePostView.as_view(), name="delete_posts"),
    path('details/<int:id>', views.DetailPostView.as_view(), name="details_post"),
]
