from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required, name="dispatch")
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_posts.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def add_posts(request):
    if (request.method == "POST"):
        add_posts = PostForm(request.POST)
        if add_posts.is_valid():
            add_posts.instance.author = request.user
            add_posts.save()
            return redirect("add_posts")
    else:
        add_posts = PostForm()
    return render(request, 'add_posts.html', {'form': add_posts})


@login_required
def edit_posts(request, id):
    post = Post.objects.get(pk=id)
    add_posts = PostForm(instance=post)

    if (request.method == "POST"):
        add_posts = PostForm(request.POST, instance=post)
        if add_posts.is_valid():
            add_posts.instance.author = request.user
            add_posts.save()
            return redirect("home")

    return render(request, 'add_posts.html', {'form': add_posts})


@login_required
def delete_posts(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect("home")
