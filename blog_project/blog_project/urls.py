from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('profile/', include("profiles.urls")),
    path('author/', include("authors.urls")),
    path('post/', include("posts.urls")),
    path('category/', include("categories.urls")),
]
