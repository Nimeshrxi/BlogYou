from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from posts.models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})

@login_required

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
            
    return  render(request, "posts/post_create.html", {"form": form})