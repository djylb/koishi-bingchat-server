#!/bin/sh
# `/sbin/setuser www-data` runs the given command as the user `www-data`.
cd /srv/openchat || exit

python3 -m venv venv && \
. venv/bin/activate && \
pip3 install -U pip && \
pip3 install wheel && \
pip3 install --upgrade  -r requirements.txt

if [ ! -d "/srv/openchat/log/" ];then
    exec /srv/openchat/venv/bin/python /srv/openchat/bing.py >> /dev/null 2>&1
else
    exec /srv/openchat/venv/bin/python /srv/openchat/bing.py >> /srv/openchat/log/$(date "+%Y%m%d-%H%M%S").log 2>&1
fi

