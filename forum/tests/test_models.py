from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import Post, Profile

User = get_user_model()

class TestModels(TestCase):
    
    def test_is_empty(self):
        """Ensuring there is no record in the table"""  
        saved_posts = Post.objects.all()
        saved_profile = Profile.objects.all()
        # self.assertEqual(saved_posts.count(), 0)

    def setUp(self):
        self.user_a = User(username='testuser')
        self.user_a.set_password('my_test_pwd')
        self.user_a.save()
        user_count = User.objects.all().count()
        saved_profile = Profile.objects.all().count()
        # print(f"user count:{user_count}")
        # self.assertEqual(user_count, 1)
        # self.assertNotEqual(user_count, 0)
        # """Ensure that profile is created upon user register"""
        # self.assertEquals(saved_profile, 1)
        self.post1 = Post.objects.create(
                                        title = 'test title1',
                                        location = 'somewhere',
                                        author = self.user_a,
                                        excerpt = 'test excerpt',
                                        content = 'test content'
                                        ) 
        self.profile = Profile.objects.create(
                                            about_me = 'self introduction',
                                            about_dog = 'Introduction of dog'
                                            )

    def test_user_and_profile_create(self):
        """Ensure user is created and its profile record is genrerated"""
        user_count = User.objects.all().count()
        saved_profile = Profile.objects.all().count()
        print(f"user count:{user_count}")
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
        self.assertEquals(saved_profile, 1)

    def test_slug_generated_on_post_create(self):
        """
        Tesing slug is generated on post create based on title
        """
        self.assertEquals(self.post1.slug, 'test-title1')

    def test_status_set_to_post(self):
        self.assertEquals(self.post1.status, 0)

    # def test_profile_edit(self):
    #     profile = self.profile
    #     user_a = self.user_a


              





# class UserTestCase(TestCase):
#     """Creating a test user"""

#     def setUp(self):
#         user_a = User(username='testuser', email='test@email.com')
#         user_a.is_staff = True
#         user_a.is_superuser = True
#         user_a.set_password('my_test_pwd')
#         user_a.save()

#     def test_user_exists(self):
#         """Testing to ensure that user is created"""
#         user_count = User.objects.all().count()
#         # print(user_count)
#         self.assertEqual(user_count, 1)
#         self.assertNotEqual(user_count, 0)

#     def test_user_password(self):
#         """Ensuring the user exists"""
#         user_qs = User.objects.filter(username__iexact='testuser')
#         user_exists = user_qs.exists() and user_qs.count() == 1
#         self.assertTrue((user_exists))

    

# class TestPostViews(TestCase):

#     def setUpTestData(self):
#         post : Post.objects.create(
#             title : 'test title',
#             location : 'nature trail somewhere',
#             author : User(username='testuser', password ='my_test_pwd'),
#             excerpt : 'This is my test excerpt',
#             content : 'This is my test content'
#         )
