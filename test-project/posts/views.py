from django.shortcuts import render
from django.views.generic import ListView
from .models import PostModel


class HomePageView(ListView):
    model = PostModel
    template_name = 'posts.html'
    context_object_name = 'all_posts_list'
