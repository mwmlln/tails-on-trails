from django.shortcuts import render
from django.views import generic, View
from .models import Post


def index(request):
    """ Returns index.html """
    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 6
