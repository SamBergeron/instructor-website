from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import blogPageView, postDetailView, addPostView

# for blog views
urlpatterns = patterns('blog.views',
    
    #for the blog view
    url(r'^/$', blogPageView.as_view(), name='main'),
    url(r'^/add/$', addPostView.as_view(), name='post_add'),
    url(r'^/(?P<slug>[\w-]+)/$', postDetailView.as_view(), name='post_detail'),
)
