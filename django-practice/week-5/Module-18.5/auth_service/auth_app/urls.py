from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="sign_up"),
    path("signin/", views.sign_in, name="sign_in"),
    path("profile/", views.user_profile, name="profile"),
    path("change-password/", views.change_password, name="change_password"),
    path("logout/", views.user_logout, name="logout"),
]
