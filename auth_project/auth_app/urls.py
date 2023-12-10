from django.urls import path
from .views import signup, home, userLogin, profile, userLogout

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", userLogin, name="signin"),
    path("profile/", profile, name="profile"),
    path("logout/", userLogout, name="logout")
]
