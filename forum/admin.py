from django.contrib import admin
from .models import Post, Comment,Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'location', 'slug', 'status', 'created_on')
    search_fields = ['location', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('username', 'about_me', 'about_dog', 'featured_image', 'favorite_location')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
