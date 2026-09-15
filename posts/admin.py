from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ("created_at", "author")
    search_fields = ("title", "content", "author_username")
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    list_filter = ("created_at", "author")
    search_fields = ("content",  "author__username")