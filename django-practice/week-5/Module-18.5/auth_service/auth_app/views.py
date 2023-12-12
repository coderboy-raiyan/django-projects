from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserDataForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if (request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Singed up successfully")
            form.save()
            return redirect('sign_in')
    else:
        form = RegistrationForm()

    return render(request, "auth.html", {"form": form, "type": "Sign up"})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("home")

    if (request.method == "POST"):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Singed in successfully")
                return redirect('profile')
            else:
                return redirect("sign_up")
    else:
        form = AuthenticationForm()

    return render(request, "auth.html", {"form": form, "type": "Sign in"})


@login_required
def user_profile(request):
    if (request.method == "POST"):
        form = ChangeUserDataForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated Successfully")
            return redirect("profile")
    else:
        form = ChangeUserDataForm(instance=request.user)

    return render(request, "profile.html", {"form": form, "type": "Update your profile"})


@login_required
def change_password(request):
    if (request.method == "POST"):
        form = SetPasswordForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password updated Successfully")
            return redirect("profile")
    else:
        form = SetPasswordForm(user=request.user)

    return render(request, "change_pass.html", {"form": form, "type": "Update Password"})


def user_logout(request):
    logout(request)
    messages.warning(request, "Logged out Successfully")
    return redirect("home")
