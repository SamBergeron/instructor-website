from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import homePageView

admin.autodiscover()

#base home
urlpatterns = patterns('instructor_website.views',

    url(r'^$', homePageView.as_view(), name='home'),
    url(r'^blog', include("blog.urls", namespace='blog')),
        
    #admin access for postgres
    url(r'^admin/', include(admin.site.urls)),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

