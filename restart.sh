#!/bin/sh
# stop
nginx -s stop
killall -QUIT uwsgi

# git
# git pull
# python manage_production.py collectstatic

sleep 1

# start
uwsgi -x /www/QQMusicSearcher/uwsgi.xml
nginx -c /www/QQMusicSearcher/nginx.conf