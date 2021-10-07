from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('location', 'slug', 'status', 'created_on')
    search_fields = ['location', 'content']
    prepopulated_fields = {'slug': ('location',)}
    list_filter = ('status', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
