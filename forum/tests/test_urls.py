from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from forum.views import (index, about, PostList, ProfileList, edit_profile,
                        PostDetail, create_post, delete_post, edit_post,
                        ProfileDetail
                        )


class TestUrls(SimpleTestCase):
    """
    Testing for resolving urls
    """

    def test_index_url(self):
        """Testing redirect to index page"""
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_about_url(self):
        """Testing redirect to about page"""
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_posts_url(self):
        """Testing redirect to post list"""
        url = reverse('posts')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_profile_url(self):
        """Testing redirect to profile list"""
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, ProfileList)

    def test_edit_profile_url(self):
        """Testing redirect to edit profile list"""
        url = reverse('profile_edit')
        self.assertEqual(resolve(url).func, edit_profile)

    def test_profile_detail_url(self):
        """Testing redirect to proprofile detailt"""
        url = reverse('profile_detail', args=['username'])
        self.assertEqual(resolve(url).func.view_class, ProfileDetail)

    def test_create_post_url(self):
        """Testing redirect to create post list"""
        url = reverse('create_post')
        self.assertEqual(resolve(url).func, create_post)

    def test_edit_post_url(self):
        """Testing redirect to edit post detailt"""
        url = reverse('post_edit', args=['slug-name'])
        self.assertEqual(resolve(url).func, edit_post)

    def test_delete_post_url(self):
        """Testing redirect to delete post"""
        url = reverse('post_delete', args=['slug-name'])
        self.assertEqual(resolve(url).func, delete_post)

    def test_post_detailt_url(self):
        """Testing redirect to post detail"""
        url = reverse('post_detail', args=['slug-name'] )
        self.assertEqual(resolve(url).func.view_class, PostDetail)

