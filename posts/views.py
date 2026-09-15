from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def post_list(request):
    query = request.GET.get("q", "")
    
    posts = Post.objects.select_related("author").order_by("-created_at")
    
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    paginator = Paginator(posts, 5)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, "posts/post_list.html", {"page_obj": page_obj, "query": query,})

def post_details(request, post_id):
    post = get_object_or_404(Post.objects.select_related("author").prefetch_related("comments__author"), id=post_id)
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", post_id = post.id) 
    else:
        form = CommentForm()
    return render(request, "posts/post_detail.html", {"post": post, "form": form,})

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
            return redirect("post_detail", post_id=post.id) 
        
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

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    
    if request.method == "POST":
        post_id = comment.post.id  
        comment.delete()
        return redirect("post_detail", post_id=post_id)
    
    return render(request, "posts/comment_delete.html", {"comment": comment})

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, author=request.user)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        
        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=comment.post.id) 
        
    else:
        form = CommentForm(instance=comment)
        
    return render(request, "posts/comment_edit.html", {"form": form, "comment": comment,})