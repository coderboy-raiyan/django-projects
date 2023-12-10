from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')


def signup(request):
    if not request.user.is_authenticated:
        if (request.method == "POST"):
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created Successfully")
                print(form.cleaned_data)
        else:
            form = RegisterForm()
    else:
        return redirect("profile")

    return render(request, 'signup.html', {"form": form})


def userLogin(request):
    if not request.user.is_authenticated:
        if (request.method == "POST"):
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if (user is not None):
                    login(request, user)
                    return redirect("profile")
        else:
            form = AuthenticationForm()
    else:
        return redirect("profile")

    return render(request, 'login.html', {"form": form})


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {'user': request.user})
    else:
        return redirect("signin")


def userLogout(request):
    logout(request)
    return redirect("home")
