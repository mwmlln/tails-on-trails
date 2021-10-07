from django.shortcuts import render
from .models import Post
from django.views import generic, View
# from django.views.generic import TemplateView


# Create your views here.

def index(request):
    """ Returns index.html """
    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "forum.html"
    paginate_by = 6
