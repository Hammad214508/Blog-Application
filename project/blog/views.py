from django.shortcuts import render
from django.http import HttpResponse
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

def about(request):
    return render(request, 'blog/about.html')
