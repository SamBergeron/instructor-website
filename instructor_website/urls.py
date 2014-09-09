from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import homePageView

admin.autodiscover()

#base home
urlpatterns = patterns('instructor_website.views',

    url(r'^$', homePageView.as_view(), name='home'),
    url(r'^blog', include("blog.urls", namespace='blog')),
        
    #admin access for postgres
    url(r'^admin/', include(admin.site.urls)),
)
