from django.shortcuts import render_to_response
from django.views.generic import TemplateView

class homePageView(TemplateView):
    template_name = 'home.html'

    
def shred(request):
    return render_to_response('shred.html')