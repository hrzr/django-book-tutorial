from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import PostModel


class BlogTests(TestCase):
    username = 'testuser'
    email = 'test@test.test'
    password = 'secret'

    post_title = 'Nice title'
    post_body = 'Nice body'

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

        self.post = PostModel.objects.create(
            title=self.post_title,
            body=self.post_body,
            author=self.user
        )

    def test_string_representation(self):
        post = PostModel(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/blog/post-1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', self.post_title)
        self.assertEqual(f'{self.post.author}', self.username)
        self.assertEqual(f'{self.post.body}', self.post_body)

    def test_post_list_view(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post_body)
        self.assertTemplateUsed(response, 'blog_index.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/post-1/')
        no_response = self.client.get('/blog/post-100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.post_title)
        self.assertTemplateUsed(response, 'blogpost_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(PostModel.objects.first().title, 'New title')
        self.assertEqual(PostModel.objects.first().body, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('post_delete', args='1')
        )
        self.assertEqual(response.status_code, 302)
