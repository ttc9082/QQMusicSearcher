from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('main.views',
    url(r'^music/$', 'music', name='music'),
    url(r'^live/$', 'live', name='live'),
    url(r'^alert/$', 'xss', name='xss'),
    url(r'^xss/$', 'alert', name='alert'),
)