from django.test import TestCase
from .models import Post


class TestModels(TestCase):
    def setUp(self):
        Post.objects.create(location="Test Forum Post", slug="slug" )
        Post.objects.create(excerpt="This is test summary")

    def test_posts_creates_correct(self):

        post1 = Post.objects.get(location="Test Forum Post")
        self.assertEqual(post1.status, 0)
        post2 = Post.objects.get(location="This is test summary")
        self.assertEqual(post2.difficulty_easy, True)
        
