from django.contrib import admin
from django.urls import path, include
from .views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/', include("categories.urls")),
    path('category/<slug:category_slug>/', home, name='category_slug'),
    path('author/', include("authors.urls")),
    path('post/', include("posts.urls")),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
