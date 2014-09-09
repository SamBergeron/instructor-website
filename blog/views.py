from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class publishedPostMixin(object):
    def get_queryset(self):
        queryset = super(publishedPostMixin, self).get_queryset()
        return queryset.filter(published=True)    

class blogPageView(publishedPostMixin, ListView):
    model = Post
    template_name = 'blog.html'
        
class postDetailView(publishedPostMixin, DetailView):
    model = Post