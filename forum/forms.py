from .models import Post, Comment, Profile
from django.core import validators
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(
                            label='Post Title',
                            max_length=200,
                            widget=forms.TextInput(attrs={
                                'placeholder':
                                'Your unique post title',
                                },))
    location = forms.CharField(label='Location', max_length=50)
    excerpt = forms.CharField(
                            label='Summary of your post',
                            max_length=300,
                            widget=forms.Textarea,
                            required=False)
    content = forms.CharField(
                            label='Post Content',
                            max_length=1500,
                            widget=forms.Textarea)
    difficulty_hard = forms.BooleanField(label='Hard', required=False)
    difficulty_moderate = forms.BooleanField(label='Moderate', required=False)
    difficulty_easy = forms.BooleanField(label='Easy', required=False)
    breed_big = forms.BooleanField(label='Big', required=False)
    breed_mid = forms.BooleanField(label='Medium', required=False)
    breed_sml = forms.BooleanField(label='Small', required=False)

    class Meta:
        model = Post
        fields = (
            'title', 'location', 'excerpt',
            'featured_image', 'content', 'difficulty_hard',
            'difficulty_moderate', 'difficulty_easy',
            'breed_big', 'breed_mid', 'breed_sml')

    def clean_title(self):
        """checks if title entered exists already"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        is_exists = Post.objects.filter(title__iexact=title).first()
        if is_exists:
            raise validators.ValidationError(
                                            'This title already exists.'
                                            'Please enter another one.')
        return title


class EditPostForm(forms.ModelForm):
    title = forms.CharField(label='Post Title', max_length=200)
    location = forms.CharField(label='Location', max_length=50)
    excerpt = forms.CharField(
                            label='Summary of your post',
                            max_length=300,
                            widget=forms.Textarea,
                            required=False)
    content = forms.CharField(
                            label='Post Content',
                            max_length=1500,
                            widget=forms.Textarea)
    difficulty_hard = forms.BooleanField(label='Hard', required=False)
    difficulty_moderate = forms.BooleanField(label='Moderate', required=False)
    difficulty_easy = forms.BooleanField(label='Easy', required=False)
    breed_big = forms.BooleanField(label='Big', required=False)
    breed_mid = forms.BooleanField(label='Medium', required=False)
    breed_sml = forms.BooleanField(label='Small', required=False)

    class Meta:
        model = Post
        fields = (
            'title', 'location', 'excerpt',
            'featured_image', 'content', 'difficulty_hard',
            'difficulty_moderate', 'difficulty_easy',
            'breed_big', 'breed_mid', 'breed_sml')

    def clean_title(self):
        """checks if title entered exists already"""
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        is_exists = Post.objects.filter(title__iexact=title).first()
        if is_exists:
            raise validators.ValidationError(
                                            'This title already exists.'
                                            'Please enter another one.')
        return title


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class ProfileEditForm(forms.ModelForm):

    featured_image = forms.FileField(label='Image')
    about_me = forms.CharField(
                            label='About Me:',
                            required=False,
                            max_length=300,
                            widget=forms.Textarea)
    about_dog = forms.CharField(
                            label='About My Dog(s):',
                            required=False,
                            max_length=300,
                            widget=forms.Textarea)
    favorite_location = forms.CharField(
                                    label='My Favorite Location:',
                                    required=False,
                                    max_length=100,
                                    widget=forms.Textarea, )

    class Meta:
        model = Profile
        fields = (
                'featured_image', 'about_me',
                'about_dog', 'favorite_location')
