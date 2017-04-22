#!/bin/bash

NAME="wmendezblog"                                  # Name of the application
DJANGODIR=/home/srvnginx/                        # Django project directory
SOCKFILE=/tmp/gunicorn.sock                     # we will communicte using this unix socket
LOGDIR=${DJANGODIR}logs/gunicorn/gunicorn.log
USER=srvnginx                                   # the user to run as
GROUP=srvnginx                                   # the group to run as
NUM_WORKERS=5                                   # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=srvnginx.config.settings.production         # which settings file should Django use
DJANGO_WSGI_MODULE=srvnginx.wsgi                 # WSGI module name

rm -frv $SOCKFILE

echo "Starting $NAME as `whoami`"

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)

cd $DJANGODIR

exec /usr/local/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR

0
