from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Post


# Create your tests here.


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret")

        cls.post = Post.objects.create(
            title="A Good Title",
            body="Nice Body Content",
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A Good Title")
        self.assertEqual(self.post.body, "Nice Body Content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A Good Title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
