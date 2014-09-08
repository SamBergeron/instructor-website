from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views
admin.autodiscover()

#base home
urlpatterns = patterns('instructor_website.views',

    url(r'^$', views.homePageView.as_view(), name='home'),
    url(r'^blog/$', views.blogPageView.as_view(), name='blog'),
    url(r'^shred/$', 'shred', name='shred'),
    
    #admin access for postgres
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',
)
