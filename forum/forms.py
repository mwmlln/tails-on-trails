from .models import Post, Comment, Profile
from django.core import validators
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(
                            label='Post Title',
                            widget=forms.TextInput(attrs={
                                'placeholder':
                                'Your post title here',
                                'class': 'create-post'
                                },))
    location = forms.CharField(label='Location')
    excerpt = forms.CharField(label='Summary of your post', widget=forms.Textarea)
    content = forms.CharField(label='Post Content', widget=forms.Textarea)
    difficulty_hard = forms.BooleanField(label='Hard', required=False )
    difficulty_moderate = forms.BooleanField(label='Moderate', required=False)
    difficulty_easy = forms.BooleanField(label='Easy', required=False)
    breed_big = forms.BooleanField(label='Big', required=False)
    breed_mid = forms.BooleanField(label='Medium', required=False)
    breed_sml = forms.BooleanField(label='Small', required=False)

    class Meta:
        model = Post
        fields = ('title', 'location', 'excerpt',
        'featured_image', 'content','difficulty_hard',
        'difficulty_moderate','difficulty_easy',
        'breed_big', 'breed_mid','breed_sml' )

    def clean_title(self):
        """checks if title entered already exisits already"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        is_exists = Post.objects.filter(title=title).first()
        if is_exists:
            raise validators.ValidationError('This title already exists.' 
                                            ' Please enter another one.')
        return title


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
