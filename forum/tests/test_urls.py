from django.test import TestCase
from django.urls import reverse, resolve
from ..views import index, PostList, PostDetail

# This test is not working ==== Need to fix ====
class TestUrls(TestCase):

  def test_post_index_url(self):
      """Testing redirect to index page"""
      view = resolve('')
      self.assertEqual(view.func.view_class, index)
  
  def test_post_list_url(self):
      """Testing redirect to post_list"""
      view = resolve('posts')
      self.assertEqual(view.func.view_class, PostList)
      

  def test_post_list_url(self):
      """Testing redirect to post_detail"""
      response = self.client.get(reverse('post_detail', args=(test.slug,)))
      self.assertEqual(view.func.view_class, PostDetail)
    