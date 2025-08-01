from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testUser')
        self.post = Post.objects.create(
            author=self.user,
            title='Test Title',
            content='Test Content'
        )
        

    def test_post_creation(self):
        self.assertEqual(self.post.title,'Test Title')
