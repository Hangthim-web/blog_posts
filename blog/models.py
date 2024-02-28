from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.user",
        on_delete = models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title;

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"pk" :self.pk})


    def test_url_exists_at_current_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_url_exists_at_current_location(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code,200);

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.contains(response,"Nice Body Content")
        self.assertTemplateUsed(response,"home.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("post_Detail",kwargs={"pk" : self.post.pk}))
        no_response = self.client.get("/post/10000/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"A Good Title")
        self.assertTemplateUsed(response,"post_detail.html")

