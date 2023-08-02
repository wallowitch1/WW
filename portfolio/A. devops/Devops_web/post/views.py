from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/post/'
    template_name = 'post/post_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def check_auth(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    def check_auth(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    success_url = reverse_lazy('post_list')
