from django.conf.urls import patterns, include, url
from django.contrib import admin
from status import urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'laundry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^status/', include(urls, namespace="status")),
)
