from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from forum.models import Post, Profile

User = get_user_model()


class TestViews(TestCase):
    """Setting up testing data"""

    def setUp(self):
        self.client = Client()
        self.posts_url = reverse('posts')
        self.user_a = User(username='testuser')
        self.user_a.set_password('my_test_pwd')
        self.client.login(username='testuser', password='my_test_pwd')
        self.user_a.save()
        self.post_1 = Post.objects.create(
            author=self.user_a,
            title='test post',
            excerpt='test post'
        )
        self.post_detail_url = reverse('post_detail', args=['test-post'])
        self.post_createl_url = reverse('create_post')
        self.post_edit_url = reverse('post_edit', args=['test-post'])
        self.post_delete_url = reverse('post_delete', args=['test-post'])
        self.profiles_url = reverse('profile')
        self.profile_detail_url = reverse('profile_detail', args=['user_a'])

    def test_get_home(self):
        """Testing Index page url"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about(self):
        """Testing About page url"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_post_list_GET(self):
        """Testing Post List page url"""
        self.client.logout()
        response = self.client.get(self.posts_url)
        queryset = Post.objects.filter(status=1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_redirect_GET(self):
        """
        Testing post detail page to redirect for non login users
        """
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_post_detail_registered_GET(self):
        """
        Testing to post detail page display for login users
        """
        self.client.login(username='testuser', password='my_test_pwd')
        post = self.post_1
        response = self.client.get(self.post_detail_url)
        self.assertEqual(self.post_1.slug, 'test-post')

    def test_post_detail_POST_no_data(self):
        response = self.client.post(self.post_detail_url)
        user = self.user_a
        self.assertEquals(response.status_code, 404)
        self.assertEquals(self.post_1.title.count('test-post'), 0)

    def test_post_edit(self):
        self.client.login(username='testuser', password='my_test_pwd')
        post = self.post_1
        response = self.client.get(self.post_edit_url)
        self.assertTemplateUsed(response, 'post_edit.html')

    def test_profile_detail_redirect_GET(self):
        """
        Testing profile detail page to redirect for non login users
        """
        client = Client()
        client.logout()
        response = self.client.get(self.profile_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_profile_detal_registered_GET(self):
        """
        Testing to profile detail page display for login users
        """
        user = self.user_a
        client = Client()
        client.force_login(self.user_a)
        profile = Profile.objects.get(user=user)
        response = self.client.get(f'/profile/{user}')
        self.assertEqual(response.status_code, 302)
