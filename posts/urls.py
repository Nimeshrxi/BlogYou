from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:post_id>/", views.post_details, name="post_detail"), # type: ignore
]