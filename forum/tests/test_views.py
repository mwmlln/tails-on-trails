from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from forum.models import Post, Profile
import json

User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.posts_url = reverse('posts')
        user_a = User(username='testuser')
        user_a.set_password('my_test_pwd')
        user_a.save()
        self.post_1 = Post.objects.create(
            author = user_a,
            title = 'Test post',
            excerpt = 'test post'
        )
        self.post_detail_url = reverse('post_detail', args=['test-post'])


    def test_get_home(self):
        print('test_get_home')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about(self):
        print('test_get_about')
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')


    def test_post_list_GET(self):
        print('test_get_posts')
        response = self.client.get(self.posts_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')


    # def test_post_detail_GET(self):
    #     """
    #     ======== NOT WORKING  ==========
    #     """
    #     print('test_get_posts_detail')
    #     response = self.client.get(self.post_detail_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'post_detail.html')

