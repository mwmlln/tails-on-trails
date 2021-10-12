from django.test import TestCase
from forum.models import Post


class TestModels(TestCase):
    def test_is_empty(self):
        """Ensuring there is no record in the table"""  
        saved_posts = Post.objects.all()
        self.assertEqual(saved_posts.count(), 0)


    # def test_is_count_one(self):
    #     """Test to ensure creating an entry will returns one record in the table"""
    #     post = Post(location='test_location', slug='test_slug1')
    #     post.save()
    #     saved_posts = Post.objects.all()
    #     self.assertEqual(saved_posts.count(), 1)


    # def setUp(self):
    #     Post.objects.create(location="Test Forum Post", slug="slug" )
    #     Post.objects.create(excerpt="This is test summary")

    # def test_posts_creates_correct(self):

    #     post1 = Post.objects.get(location="Test Forum Post")
    #     self.assertEqual(post1.status, 0)
    #     post2 = Post.objects.get(location="This is test summary")
    #     self.assertEqual(post2.difficulty_easy, True)
        
