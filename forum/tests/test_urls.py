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
        print('test_index_url:')
        """Testing redirect to index page"""
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_about_url(self):
        print('test_about_url:')
        """Testing redirect to about page"""
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_posts_url(self):
        print('test_posts_url:')
        """Testing redirect to post list"""
        url = reverse('posts')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_profile_url(self):
        print('test_profile_url:')
        """Testing redirect to profile list"""
        url = reverse('profile')
        self.assertEqual(resolve(url).func.view_class, ProfileList)

    def test_edit_profile_url(self):
        print('test_edit_profile_url:')
        """Testing redirect to edit profile list"""
        url = reverse('profile_edit')
        self.assertEqual(resolve(url).func, edit_profile)

    def test_profile_detail_url(self):
        print('test_profile_detail_url:')
        """Testing redirect to proprofile detailt"""
        url = reverse('profile_detail', args=['username'])
        self.assertEqual(resolve(url).func.view_class, ProfileDetail)

    def test_create_post_url(self):
        print('test_create_post_url:')
        """Testing redirect to create post list"""
        url = reverse('create_post')
        self.assertEqual(resolve(url).func, create_post)

    def test_edit_post_url(self):
        print('test_edit_post_url:')
        """Testing redirect to edit post detailt"""
        url = reverse('post_edit', args=['slug-name'])
        self.assertEqual(resolve(url).func, edit_post)

    def test_delete_post_url(self):
        print('test_delete_postl_url:')
        """Testing redirect to delete post"""
        url = reverse('post_delete', args=['slug-name'])
        self.assertEqual(resolve(url).func, delete_post)

    def test_post_detailt_url(self):
        print('test_post_ detail_url:')
        """Testing redirect to post detail"""
        url = reverse('post_detail', args=['slug-name'] )
        self.assertEqual(resolve(url).func.view_class, PostDetail)




#  ==== Not working part ====
# This test is not working
# class TestUrls(TestCase):

#     def setUp(self):
#         """Setting up a user data"""
#         user_a = User(username='testuser', email='test@email.com')
#         user_a_pwd ='my_test_pwd'
#         self.user_a_pwd = user_a_pwd
#         user_a.is_staff = True
#         user_a.is_superuser = True
#         user_a.set_password(user_a_pwd)
#         user_a.save()
#         self.user_a = user_a
#         user_b = User(username='testuser2', email='test2@email.com')
#         user_b.is_staff = False
#         user_b.is_superuser = False
#         user_b.set_password('my_test_pwd2')
#         user_b.save()
#         self.usre_b = user_b
    
    


    # def test_login_url(self):
    #     print('test_login_url:')
    #     login_url = settings.LOGIN_URL
    #     data = {'username': 'testuser', 'password': 'my_test_pwd'}
    #     response = sef.client.post(login_url, data, follow=True)
    #     status_code = resolve.status_code
    #     redirect_path = response.request.get('PATH_INFO')
    #     # self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)
    #     self.assertEqual(status_code, 200)


    # def test_invalid_request(self):
    #     """Ensures that the page is not accessible to unregistered users"""
    #     self.client.login(
    #                     username=self.user_b.username,
    #                     password='my_test_pwd2')
    #     response = serlf.client.post('/create/', 
    #                                 {'title': 'this is a invalid test' })
    # def test_invalid_request(self):
    #     print('test_invalid_request:')
    #     self.assertTrue(status_code = 200)


  
#   def test_post_list_url(self):
#       """Testing redirect to post_list"""
#       view = resolve('posts')
#       self.assertEqual(resolver.func.__name__, PostList.as_view().__name__)
      

#   def test_post_list_url(self):
#       """Testing redirect to post_detail"""
#       response = self.client.get(reverse('post_detail', args=(test.slug,)))
#       self.assertEqual(resolver.func.__name__, PostList.as_view().__name__)
    