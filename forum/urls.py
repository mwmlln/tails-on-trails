from . import views
from django.urls import path

# app_name = 'forum'

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('create/', views.create_post, name='create_post'),
    path('edit_post/<slug:slug>', views.edit_post, name='post_edit'),
    path('delete_post/<slug:slug>', views.delete_post, name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
  ]