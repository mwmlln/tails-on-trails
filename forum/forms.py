from .models import Post, Comment, Profile
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(label='Title')

    class Meta:
        model = Post
        fields = ('title', 'location', 'excerpt',
        'featured_image', 'content','difficulty_hard',
        'difficulty_moderate','difficulty_easy',
        'breed_big', 'breed_mid','breed_sml' )


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class ProfileForm(forms.ModelForm):  

    class Mata:
        model = Profile
        fields = '__all__'


class ProfileEditForm(forms.ModelForm):

    featured_image = forms.FileField(label='Image')
    about_me = forms.CharField(label='About Me:')
    about_dog = forms.CharField(label='About My Dog(s):')
    favorite_location = forms.CharField(label='My Favorite Location:', max_length=300)

    class Meta:
        model = Profile
        fields = ('featured_image','about_me','about_dog', 'favorite_location')
