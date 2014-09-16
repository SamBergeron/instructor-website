from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from .models import Post, PostForm

class publishedPostMixin(object):
    def get_queryset(self):
        queryset = super(publishedPostMixin, self).get_queryset()
        return queryset.filter(published=True)    

class blogPageView(publishedPostMixin, ListView):
    model = Post
    template_name = 'blog.html'
        
class addPostView(CreateView):
    form_class = PostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog:main')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.author = self.request.user
        return super(addPostView, self).form_valid(form)
    
class postDetailView(publishedPostMixin, DetailView):
    model = Post
