from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_get_post_list(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_get_post_detail(self):
        response = self.client.get(reverse('post_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')