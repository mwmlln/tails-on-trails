# from django.test import SimpleTestCase, TestCase
# from forum.forms import CommentForm, CreatePostForm, EditPostForm
# from forum.forms import DeletePostForm,  ProfileEditForm


# class CreatePostForm(TestCase):

#     def test_title_entry_is_required(self):
#         form = CreatePostForm({'title': ''})
#         self.assertFalse(form.is_valid())
#         self.assertIn('title', form.errors.keys())
#         self.assertEqual(form.errors['title'][0], 'This fiels is required.')

#     def test_location_field_is_not_required(self):
#         form = CreatePostForm({'title': 'test title'})
#         self.assertTrue(form.is_valid())

#     def test_fields_are_explicit_in_form_mataclass(self):
#         form = CreatePostForm()
#         self.assertEqual(form.Mata.fields, [
#                                         'title',
#                                         'location',
#                                         'excerpt',
#                                         'featured_image',
#                                         'content',
#                                         'difficulty_hard',
#                                         'difficulty_moderate',
#                                         'difficulty_easy',
#                                         'breed_big',
#                                         'breed_mid',
#                                         'breed_sml'
#                                     ])


# # class TestForms(SimpleTestCase):

# #     def test_create_post_valid_data(self):
# #         form = CreatePostForm(data={
# #             'title': 'my post',
# #             'location' : 'test location',
# #             'content' : 'my test post'
# #         })

# #         self.assertTrue(form.is_valid())

# #     def test_create_post_no_data(self):
# #         form = CreatePostForm(data={})

# #         self.assertFalse(form.is_valid())
# #         self.assertEquals(len(form.errors), 3)


