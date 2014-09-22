from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import loginView, homePage, mailingListForm

admin.autodiscover()

#base home
urlpatterns = patterns('instructor_website.views',

    url(r'^$', homePage.as_view(), name='home'),
    url(r'^mailing-list/', mailingListForm.as_view(), name='mailing-list'),
    url(r'^blog', include("blog.urls", namespace='blog')),
    url(r'^login/', loginView.as_view(), 'django.contrib.auth.views.login'),
        
    #admin access for postgres
    url(r'^admin/', include(admin.site.urls)),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

