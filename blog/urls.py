from django.conf.urls import patterns, include, url

from .views import blogPageView, postDetailView

# for blog views
urlpatterns = patterns('blog.views',
    
    #for the blog view
    url(r'^/$', blogPageView.as_view(), name='main'),
    url(r'^/(?P<slug>[\w-]+)/$', postDetailView.as_view(), name='post_detail'),
)