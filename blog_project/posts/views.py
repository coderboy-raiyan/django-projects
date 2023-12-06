from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
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


def edit_posts(request, id):
    post = Post.objects.get(pk=id)
    add_posts = PostForm(instance=post)

    if (request.method == "POST"):
        add_posts = PostForm(request.POST, instance=post)
        if add_posts.is_valid():
            add_posts.save()
            return redirect("home")

    return render(request, 'add_posts.html', {'form': add_posts})


def delete_posts(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("home")
