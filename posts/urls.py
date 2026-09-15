from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("create/", views.post_create, name="post_create"),
    path("register/", views.register, name="register"),
    path("<int:post_id>/", views.post_details, name="post_detail"), # type: ignore
    path("<int:post_id>/edit/", views.post_edit, name="post_edit"),
    path("<int:post_id>/delete/", views.post_delete, name="post_delete"),
    path("comment/<int:comment_id>/delete/", views.comment_delete, name="comment_delete"),
    path("comment/<int:comment_id>/edit/", views.comment_edit, name="comment_edit"),
]