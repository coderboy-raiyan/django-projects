from django.shortcuts import render, redirect
from .forms import ProfileForm
# Create your views here.


def add_profiles(request):
    if (request.method == "POST"):
        add_profiles = ProfileForm(request.POST)
        if add_profiles.is_valid():
            add_profiles.save()
            return redirect("add_profiles")
    else:
        add_profiles = ProfileForm()
    return render(request, 'add_profiles.html', {'form': add_profiles})
