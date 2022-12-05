from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import PostModel


class BlogListView(ListView):
    model = PostModel
    template_name = 'blog_index.html'


class BlogDetailView(DetailView):
    model = PostModel
    template_name = 'blogpost_detail.html'
    context_object_name = 'post'
