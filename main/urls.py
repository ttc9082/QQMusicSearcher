from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('main.views',
    url(r'^music/$', 'music', name='music'),
)