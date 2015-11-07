#!/bin/sh
# stop
nginx -s stop
killall -QUIT uwsgi

# git
# git pull
# python manage_production.py collectstatic

sleep 1

# start
uwsgi -x /home/tongtianqi/uwsgi.xml
nginx -c /home/tongtianqi/nginx.conf