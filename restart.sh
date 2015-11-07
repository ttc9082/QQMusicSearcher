#!/bin/sh
# stop
nginx -s stop
killall -QUIT uwsgi

# git
# git pull
# python manage_production.py collectstatic

sleep 1

# start
uwsgi -x /home/tong28/ddw/production_uwsgi.xml
nginx -c /home/tong28/ddw/production_nginx.conf