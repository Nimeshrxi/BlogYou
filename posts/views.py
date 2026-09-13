from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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
            post.save()
            return redirect("post_list")
    else:
        form = PostForm()
            
    return  render(request, "posts/post_create.html", {"form": form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=post.id) #type: ignore
        
    else:
        form = PostForm(instance=post)
    
    return render(request, "posts/post_edit.html", {"form": form, "post": post})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    return render(request, "posts/post_delete.html", {"post": post})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
        
    return render(request, "registration/register.html", {"form": form})