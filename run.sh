#!/bin/bash
set -e
export LANG=en_US.utf8
export LC_ALL=en_US.UTF-8
export LC_LANG=en_US.UTF-8

LOGFILE=/home/gogo/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
DANGO_WSGI_MODULE=gogo.wsgi
NUM_WORKERS=3
# user/group to run as
USER=root
# GROUP=gogo
cd /home/webapps/gogo/gogo
. ../gogo_venv/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec ../gogo_venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application --timeout 400 -w $NUM_WORKERS \
--user=$USER --log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE -b 127.0.0.1:8002 .

