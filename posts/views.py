from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name ='home.html'
    # instead of object_list we use all_posts_list
    context_object_name = 'all_posts_list'
