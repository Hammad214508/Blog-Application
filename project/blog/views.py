from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
# Create a  function to manage the traffic from the home
from .models import Post
# Takes a request and return what you want the user to see

# Dummy data
# posts = [
#     {
#         'author': 'Hammad',
#         'title': 'blog post',
#         'content': 'Frist post',
#         'date_posted': '17 January 2020'
#     },
#     {
#         'author': 'Aadya',
#         'title': 'blog post',
#         'content': 'Second post',
#         'date_posted': '11 March 2020'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/model_<viewtype>/html
    context_object_name = 'posts' # context are called posts
    ordering = ['-date_posted'] #To order the posts, newst first


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # Creating a  post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # Creating a  post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # Only the creater can update the posts

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'blog/about.html')
