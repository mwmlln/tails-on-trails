from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import CommentForm, CreatePostForm
from . import forms
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Post



def index(request):
    """ Returns index.html """
    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 6


class PostDetail(View):
    """Only available for logged-in users"""
    @method_decorator(login_required, name='home')
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

    
class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def create_post(request):
    create_post_form = forms.CreatePostForm(request.POST or None)
    if create_post_form.is_valid():
        create_post_form.instance.slug = ('title',)
        create_post_form.instance.author = request.user
        create_post_form.save()
        return redirect('posts')
    return render(
        request, 'post_create.html', context= {
        'create_post_form': create_post_form,
    })


# class PostCreate(CreateView):
#     template_name = 'post_create.html'
#     model = Post
#     fields = [
#         'title',
#         'location', 
#         'excerpt', 
#         'featured_image',
#         'content',
#     ]
#     prepopulated_fields = {'slug': ('title',)}
#     if 
#     success_url = reverse_lazy('posts')


    


# @login_required
# def profile_create(request):
#     form = forms.ProfileModelForm()
#     return render(
#         request, profile.html, context= { form:form }
#         )