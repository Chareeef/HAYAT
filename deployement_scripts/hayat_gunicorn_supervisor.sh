#!/usr/bin/env bash
# Set supervisor to ensure that gunicorn is always running our HAYAT Flask app

last_update=$(stat -c %Y /var/lib/apt/periodic/update-success-stamp 2>/dev/null || stat -c %Y /var/cache/apt/pkgcache.bin 2>/dev/null)

current_time=$(date +%s)
update_threshold=$((24 * 60 * 60))  # 24 hours in seconds

if [ "$((current_time - last_update))" -gt "$update_threshold" ]; then
    sudo apt update
fi

if ! dpkg -l | grep -q supervisor; then
    sudo apt install supervisor -y
fi

sudo mkdir -p /var/log/HAYAT
sudo rm -rf /var/log/HAYAT/*
sudo touch /var/log/HAYAT/HAYAT-web.out.log
sudo touch /var/log/HAYAT/HAYAT-web.err.log
sudo touch /var/log/HAYAT/HAYAT-api.out.log
sudo touch /var/log/HAYAT/HAYAT-api.err.log

sudo rm -rf /etc/supervisor/conf.d/HAYAT*

printf "# Supervisor config file to ensure our flask web app is always run by gunicorn

[program:HAYAT-web]
directory=/home/youssef/HAYAT/
command=/home/%s/HAYAT/venv/bin/gunicorn -b 0.0.0.0:8000 -w 3 app:app
environment = HAYAT_USER=crimson, HAYAT_PWD=hayat_for_all, HAYAT_HOST=localhost, HAYAT_DB=hayat_prod_db
user=%s
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stdout_logfile=/var/log/HAYAT/HAYAT-web.out.log
stderr_logfile=/var/log/HAYAT/HAYAT-web.err.log
" "$(whoami)" "$(whoami)" | sudo tee /etc/supervisor/conf.d/HAYAT-web.conf >/dev/null

printf "# Supervisor config file to ensure our flask API is always run by gunicorn

[program:HAYAT-API]
directory=/home/youssef/HAYAT/
command=/home/%s/HAYAT/venv/bin/gunicorn -b 0.0.0.0:8001 -w 3 api.app:app
environment = HAYAT_USER=crimson, HAYAT_PWD=hayat_for_all, HAYAT_HOST=localhost, HAYAT_DB=hayat_prod_db
user=%s
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stdout_logfile=/var/log/HAYAT/HAYAT-api.out.log
stderr_logfile=/var/log/HAYAT/HAYAT-api.err.log
" "$(whoami)" "$(whoami)" | sudo tee /etc/supervisor/conf.d/HAYAT-api.conf >/dev/null

sudo supervisorctl reload
