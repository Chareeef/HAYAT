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
sudo touch /var/log/HAYAT/HAYAT.out.log
sudo touch /var/log/HAYAT/HAYAT.err.log

printf "# Supervisor config file to ensure our flask app is always run by gunicorn

[program:HAYAT]
directory=/home/youssef/HAYAT/
environement=HAYAT_USER=crimson,HAYAT_PWD=hayat_for_all,HAYAT_HOST=localhost,HAYAT_DB=hayat_prod_db
command=/home/youssef/HAYAT/venv/bin/gunicorn -w 3 app:app
user=youssef
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stdout_logfile=/var/log/HAYAT/HAYAT.out.log
stderr_logfile=/var/log/HAYAT/HAYAT.err.log
" | sudo tee /etc/supervisor/conf.d/HAYAT.conf >/dev/null

sudo supervisorctl reload
