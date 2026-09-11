from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/post_detail.html", {"post": post})