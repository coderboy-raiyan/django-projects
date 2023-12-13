from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit_profile"),
    path('profile/edit/change-password/',
         views.change_pass, name="change_password"),
    path("logout/", views.user_logout, name="logout"),

]
