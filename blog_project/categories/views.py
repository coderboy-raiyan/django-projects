from django.shortcuts import render, redirect
from .forms import CategoryForm
# Create your views here.


def add_categories(request):
    if (request.method == "POST"):
        add_categories = CategoryForm(request.POST)
        if add_categories.is_valid():
            add_categories.save()
            return redirect("add_categories")
    else:
        add_categories = CategoryForm()
    return render(request, 'add_categories.html', {'form': add_categories})
