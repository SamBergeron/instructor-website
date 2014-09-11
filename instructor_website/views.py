from django.shortcuts import render_to_response
from django.views.generic import TemplateView, DetailView

# Mixin for generic query
# class PublishedPostsMixin(object):
#     def get_queryset(self):
#         queryset = super(PublishedPostsMixin, self).get_queryset()
#         return queryset.filter(published=True)
        
class homePageView(TemplateView):
    template_name = 'home.html'
    
    

    