from django.conf.urls import patterns, url

urlpatterns = patterns('status.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<query_id>\d+)/$', 'detail', name='detail')
)
