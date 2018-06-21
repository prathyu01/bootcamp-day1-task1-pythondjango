import django.conf.urls

from django.contrib import admin
from patterns import patterns

admin.autodiscover()

urlpatterns = patterns('',
                       django.conf.urls.url(r'^$', 'myblog.views.index', name='index'),
                       django.conf.urls.url(r'^post/upload.html$', 'myblog.views.post_upload', name='post_upload'),
                       django.conf.urls.url(r'^admin/doc/', django.conf.urls.include('django.contrib.admindocs.urls')),
                       django.conf.urls.url(r'^admin/', django.conf.urls.include(admin.site.urls)),
                       )