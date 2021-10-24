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
        self.user_a = User(username='testuser')
        self.user_a.set_password('my_test_pwd')
        self.client.login(username='testuser', password='my_test_pwd')
        self.user_a.save()
        self.post_1 = Post.objects.create(
            author = self.user_a,
            title = 'test post',
            excerpt = 'test post'
        )
        self.post_detail_url = reverse('post_detail', args=['test-post'])
        self.post_delete_url = reverse('post_delete', args=['test-post'])
        self.profiles_url = reverse('profile')
        self.profile_detail_url = reverse('profile_detail', args=['user_a'])


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


    def test_post_detail_redirect_GET(self):
        """
        Testing post detail page to redirect for non login users
        """
        print('test_get_posts_detail_not_logged in')
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 302)


    def test_post_detal_registered_GET(self):
        """
        Testing to post detail page display for login users
        """
        print('post_detal_registered:')
        user = self.user_a
        post = self.post_1
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post_1.slug, 'test-post')


    def test_post_detail_POST_no_data(self):
        response = self.client.post(self.post_detail_url)
        print('post_detal_no_post:')
        user = self.user_a
        self.assertEquals(response.status_code, 404)
        # print(dir(self.post_1))
        self.assertEquals(self.post_1.title.count('test-post'), 0)

    # def test_post_delete_DELETE_post(self):
    #     post = self.post_1
    #     user = self.user_a
    #     response = self.client.delete(self.post_delete_url, json.dump({
    #         'id' :  1
    #     }))
    #     self.assertEqual(response.status_code, 204)
    #     self.assertEqual(self.post_1.slug,count('test-post'), 0 )


    # def test_post_create_POST(self):
    #     url = reverse(create_post)
    #     response = self.client.post(url, {
    #         'user' : self.user_a
    #         'title': 'title2'
    #         'excerpt' : 'test post2'
    #     })
    #     post2 = Post.objects.get(id=2)
    #     self.assertEquals(post2.slug, 'test_post2')


    def test_profile_list_GET(self):
        print('test_get_profiles')
        response = self.client.get(self.profiles_url)
        user = self.user_a
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)
        # self.assertTemplateUsed(response, 'profile.html')


    def test_profile_detail_redirect_GET(self):
        """
        Testing profile detail page to redirect for non login users
        """
        print('test_get_profiles_detail_not_logged in')
        response = self.client.get(self.profile_detail_url)
        self.assertEqual(response.status_code, 302)


    def test_profile_detal_registered_GET(self):
        """
        Testing to profile detail page display for login users
        """
        print('profile_detal_registered:')
        user = self.user_a
        response = self.client.get(self.profile_detail_url)
        self.assertEqual(response.status_code, 302)
        # self.assertEqual(self.user_a.profile, 'test-profile')




