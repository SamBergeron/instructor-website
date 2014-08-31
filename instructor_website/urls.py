from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#base home
urlpatterns = patterns('instructor_website.views',
    url(r'^$', 'index', name='index'),
    url(r'^shred/$', 'shred', name='shred'),
)


urlpatterns += patterns('',
)
