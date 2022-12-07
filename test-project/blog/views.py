from blog.models import PostModel
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = PostModel
    template_name = 'blog_index.html'


class BlogDetailView(DetailView):
    model = PostModel
    template_name = 'blogpost_detail.html'
    context_object_name = 'post'


class BlogCreateView(CreateView):
    model = PostModel
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = PostModel
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    context_object_name = 'post'


class BlogDeleteView(DeleteView):
    model = PostModel
    context_object_name = 'post'
    template_name = 'post_delete.html'
    success_url = reverse_lazy('blogs')
