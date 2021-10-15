from .models import Post, Comment, Profile
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
    

# class CreateProfileForm(forms.ModelForm):  

#     class Mata:
#         model = Profile
#         fields = '__all__'