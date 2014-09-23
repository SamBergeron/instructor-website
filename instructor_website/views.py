from django.shortcuts import render_to_response
from django.views.generic import TemplateView, DetailView, FormView, View, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth import login
from django import forms

from django.core.urlresolvers import reverse, reverse_lazy
from blog.models import Profile, Follower, FollowerForm

class mailingListForm(CreateView):
    form_class = FollowerForm
    template_name = 'mailingList.html'
    success_url = reverse_lazy('mailing-list-success')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(mailingListForm, self).form_valid(form)

class mailingListSuccess(TemplateView):
    template_name = 'mailingListSuccess.html'

class homePage(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs): 
        context = super(homePage, self).get_context_data(**kwargs)
        profile = Profile.objects.get(pk=1)
        context["profile"] = profile
        context['form'] = mailingListForm()
        return context
    
    def get(self, request, *args, **kwargs):
        return super(homePage, self).get(request, *args, **kwargs)


# TODO: Login screen
class loginView(FormView):
    template_name = 'login.html'
    

    