from django.test import TestCase
from .models import PostModel
from django.urls import reverse


class PostModelTest(TestCase):
    contents_1 = 'just a test'
    contents_2 = 'another one'

    def setUp(self) -> None:
        PostModel.objects.create(text=self.contents_1)
        PostModel.objects.create(text=self.contents_2)

    def test_text_content(self) -> None:
        post = PostModel.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, self.contents_1)

        post = PostModel.objects.get(id=2)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, self.contents_2)


class HomePageView(TestCase):
    contents = 'This is another test'

    def setUp(self) -> None:
        PostModel.objects.create(text=self.contents)

    def test_view_url_exists_at_proper_locations(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

