from django.shortcuts import render_to_response
from django.views.generic import TemplateView

# Mixin for generic query
# class PublishedPostsMixin(object):
#     def get_queryset(self):
#         queryset = super(PublishedPostsMixin, self).get_queryset()
#         return queryset.filter(published=True)
        
class homePageView(TemplateView):
    template_name = 'home.html'
    
class blogPageView(TemplateView):
    template_name = 'blog.html'
    
def shred(request):
    return render_to_response('shred.html')