from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserDataForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if (request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created Successfully")
            return redirect("register")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Sign up'})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if (request.method == "POST"):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")
                return redirect("profile")
            else:
                messages.warning(request, "User not found")
                return redirect("register")
    else:
        form = AuthenticationForm()

    return render(request, 'register.html', {'form': form, 'type': 'Sign in'})


@login_required
def edit_profile(request):
    if (request.method == "POST"):
        form = ChangeUserDataForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated Successfully")
            return redirect("profile")
    else:
        form = ChangeUserDataForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})


@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'posts': data})


@login_required
def change_pass(request):
    if (request.method == "POST"):
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password updated Successfully")
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect("home")
