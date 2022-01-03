from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name = "blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name = "user-posts"),
    path('post/<int:pk>/', views.post_detail_view, name = "post-detail"),
    path('post/new/', PostCreateView.as_view(), name = "post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = "post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete"),
    path('about/', views.about, name = "blog-about"),
    path('tag/<int:pk>/', views.tagged, name="post-tagged"),
    path('post/<int:pk>/add', views.add_post_image, name = "post-add"),
]
