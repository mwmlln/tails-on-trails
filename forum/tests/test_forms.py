from django.test import SimpleTestCase, TestCase
from forum.forms import CommentForm, CreatePostForm, EditPostForm
from forum.forms import DeletePostForm,  ProfileEditForm, Comment


class TestCreatePostForm(TestCase):

    def test_title_entry_is_required(self):
        form = CreatePostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_excerpt_field_is_not_required(self):
        form = CreatePostForm({
                            'title': 'test title', 
                            'slug': 'test-title',
                            'author': 'user_a',
                            'location' : 'test',
                            'content': 'test',
                            'excerpt': ''})
        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))


class TestEditPostForm(TestCase):

    def test_excerpt_field_is_not_required(self):
        form = CreatePostForm({
                            'title': 'test title', 
                            'slug': 'test-title',
                            'author': 'user_a',
                            'location' : 'test',
                            'content': 'test',
                            'excerpt': ''})
        self.assertTrue(form.is_valid())


class TestProfileEditForm(TestCase):

    # def test_all_fields_not_required(self):
    #     form = ProfileEditForm({
    #                         'featured_image': '',
    #                         'about_me': '',
    #                         'about_dog': '',
    #                         'favorite_location': '',})
    #     self.assertTrue(form.is_valid()) 

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProfileEditForm()
        self.assertEqual(form.Meta.fields, ('featured_image', 'about_me',
                                            'about_dog', 'favorite_location'))




