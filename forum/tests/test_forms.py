from django.test import SimpleTestCase
from forum.forms import CommentForm, CreatePostForm, EditPostForm
from forum.forms import DeletePostForm,  ProfileEditForm


# class TestForms(SimpleTestCase):

#     def test_create_post_valid_data(self):
#         form = CreatePostForm(data={
#             'title': 'my post',
#             'location' : 'test location',
#             'content' : 'my test post'
#         })

#         self.assertTrue(form.is_valid())

#     def test_create_post_no_data(self):
#         form = CreatePostForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEquals(len(form.errors), 3)


