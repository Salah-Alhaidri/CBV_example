from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,DeleteView

class post_list(ListView):
    model=Post
    template_name='post_list.html'
    

class postdetails(DetailView):
    model=Post
    template_name='post_list.html'
