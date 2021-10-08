from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    # path('signup/', signup),
  ]