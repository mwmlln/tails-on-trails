from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    # path('posts/', Posts.as_views, name='posts'),
    # path('signup/', signup),
  ]