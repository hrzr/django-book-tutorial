from django.shortcuts import render
from django.views.generic import ListView
from blog.models import PostModel


class BlogListView(ListView):
    model = PostModel
    template_name = 'blog_index.html'
