from django.urls import path
from .views import home, get_cookie, delete_cookie

urlpatterns = [
    path("", home, name="home"),
    path("get-cookie/", get_cookie, name="get_cookie"),
    path("delete-cookie/", delete_cookie, name="delete_cookie")
]
