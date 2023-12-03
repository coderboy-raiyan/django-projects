from django.shortcuts import render
from .forms import DetailsForm


def home(request):
    if (request.method == "POST"):
        name = request.POST.get("username")
        password = request.POST.get("password")
        return render(request, 'home.html', {'username': name, 'pass': password})
    else:
        return render(request, 'home.html')


def about(request):
    if (request.method == "POST"):
        name = request.POST.get("username")
        password = request.POST.get("password")
        return render(request, 'about.html', {'username': name, 'pass': password})
    else:
        return render(request, 'about.html')


def django_form(request):
    form = DetailsForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'django_form.html', {'form': form})
