from django.shortcuts import render_to_response
from django.views.generic import TemplateView, DetailView, FormView
from django.contrib.auth import login

from blog.models import Profile

# Mixin for generic query
# class PublishedPostsMixin(object):
#     def get_queryset(self):
#         queryset = super(PublishedPostsMixin, self).get_queryset()
#         return queryset.filter(published=True)
        
class homePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs): 
        context = super(homePageView, self).get_context_data(**kwargs)
        profile = Profile.objects.get(pk=1)
        context["profile"] = profile
        return context

class loginView(FormView):
    template_name = 'login.html'
    

    