from django.test import TestCase
from .models import Post


class TestModels(TestCase):

    def test_status_defaults_to_draft(self):
        post = Post.objects.create(location='Test Forum Post')
        self.assertFalse(post.status)

    def test_post_string_method_returns_name(self):
        post = Post.objects.create(location='Test Forum Post')
        self.assertEqual(str(post), 'Test Forum Post')
        