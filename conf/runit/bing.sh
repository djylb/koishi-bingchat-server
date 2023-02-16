#!/bin/sh
# `/sbin/setuser www-data` runs the given command as the user `www-data`.
cd /srv/openchat || exit
exec /sbin/setuser www-data /srv/openchat/venv/bin/python /srv/openchat/bing.py >> /dev/null 2>&1
