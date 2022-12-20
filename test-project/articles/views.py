from django.urls import reverse_lazy
from .models import Article
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Article
    fields = ('title', 'body', )
    template_name = 'article_edit.html'

    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
