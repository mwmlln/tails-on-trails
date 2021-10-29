from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import Post, Profile

User = get_user_model()


class TestModels(TestCase):

    def setUp(self):
        self.user_a = User(username='testuser')
        self.user_a.set_password('my_test_pwd')
        self.user_a.save()
        user_count = User.objects.all().count()
        saved_profile = Profile.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
        """Ensure that profile is created upon user register"""
        self.assertEqual(saved_profile, 1)
        self.post1 = Post.objects.create(
                                        title='test title1',
                                        location='somewhere',
                                        author=self.user_a,
                                        excerpt='test excerpt',
                                        content='test content'
                                        )

    def test_user_and_profile_create(self):
        """Ensure user is created and its profile record is genrerated"""
        user_count = User.objects.all().count()
        saved_profile = Profile.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)
        self.assertEqual(saved_profile, 1)

    def test_saving_and_retrieving_post(self):
        """Ensuring post is saved and retreived"""
        saved_post = Post.objects.all()
        actual_post = saved_post[0]
        self.assertEqual(actual_post.title, self.post1.title)
        self.assertEqual(actual_post.location, self.post1.location)
        self.assertEqual(actual_post.content, self.post1.content)

    def test_post_exists(self):
        """Testing to ensure that post is created"""
        post_count = Post.objects.all().count()
        self.assertEqual(post_count, 1)
        self.assertEqual(self.post1.title, 'test title1')
        self.assertEqual(self.post1.difficulty_easy, False)

    def test_slug_generated_on_post_create(self):
        """
        Tesing slug is generated on post create based on title
        """
        self.assertEquals(self.post1.slug, 'test-title1')

    def test_status_set_to_post(self):
        """New posts set to status to 0"""
        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 1)
        self.assertEquals(self.post1.status, 0)

    def post_title_max_length(self):
        post1 = Post.objects.get(id=1)
        max_length = post1._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_post_edit_updates(self):
        """Ensure editing post update the value"""
        self.post1 = Post.objects.get(id=1)
        self.post1.title = 'New title'
        self.post1.location = 'New location'
        self.post1.save()
        self.assertEquals(self.post1.title, 'New title')
        self.assertEquals(self.post1.location, 'New location')

    def test_profile_edit(self):
        """Generated profile fields have no entry"""
        self.saved_profile = Profile.objects.get(id=1)
        self.assertEquals(self.saved_profile.about_me, '')
        self.saved_profile.about_me = 'test introduction'
        self.saved_profile.about_dog = 'dog introduction'
        self.saved_profile.save()
        self.assertEquals(self.saved_profile.about_me, 'test introduction')
        self.assertEquals(self.saved_profile.about_dog, 'dog introduction')
