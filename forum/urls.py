from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
  ]