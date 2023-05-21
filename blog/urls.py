from django.urls import path
from . import views  # in current directory import views.py file
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog-about"),
]
