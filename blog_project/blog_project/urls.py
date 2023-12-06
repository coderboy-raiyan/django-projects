from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include("profiles.urls")),
    path('author/', include("authors.urls")),
    path('post/', include("posts.urls")),
    path('category/', include("categories.urls")),
]
