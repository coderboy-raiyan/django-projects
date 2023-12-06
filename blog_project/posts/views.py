from django.shortcuts import render, redirect
from .forms import PostForm
# Create your views here.


def add_posts(request):
    if (request.method == "POST"):
        add_posts = PostForm(request.POST)
        if add_posts.is_valid():
            add_posts.save()
            return redirect("add_posts")
    else:
        add_posts = PostForm()
    return render(request, 'add_posts.html', {'form': add_posts})
