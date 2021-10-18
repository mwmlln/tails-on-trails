from . import views
from django.urls import path

# app_name = 'forum'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('profile/', views.ProfileList.as_view(), name='profile'),
    path('edit_profile', views.edit_profile, name='profile_edit'),
    path('create/', views.create_post, name='create_post'),
    path('edit_post/<slug:slug>', views.edit_post, name='post_edit'),
    path('delete_post/<slug:slug>', views.delete_post, name='post_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
  ]