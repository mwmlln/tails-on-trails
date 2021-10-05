from . import views
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', views.index, name='home')
  ]