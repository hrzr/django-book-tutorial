from django.shortcuts import render
from django.views.generic import ListView
from .models import PostModel


class HomePageView(ListView):
    model = PostModel
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
