#!/usr/bin/env bash
# Set systemd to ensure that gunicorn is always running our HAYAT Flask app

last_update=$(stat -c %Y /var/lib/apt/periodic/update-success-stamp 2>/dev/null || stat -c %Y /var/cache/apt/pkgcache.bin 2>/dev/null)

current_time=$(date +%s)
update_threshold=$((24 * 60 * 60))  # 24 hours in seconds

if [ "$((current_time - last_update))" -gt "$update_threshold" ]; then
    sudo apt update
fi


sudo mkdir -p /var/log/HAYAT
sudo rm -rf /var/log/HAYAT/*
sudo touch /var/log/HAYAT/HAYAT-web.out.log
sudo touch /var/log/HAYAT/HAYAT-web.err.log
sudo touch /var/log/HAYAT/HAYAT-api.out.log
sudo touch /var/log/HAYAT/HAYAT-api.err.log
sudo chown -R $(whoami):$(whoami) /var/log/HAYAT

printf "[Unit]
Description=HAYAT Web Application
After=network.target

[Service]
User=%s
Group=%s
WorkingDirectory=/home/youssef/HAYAT/
Environment=\"HAYAT_USER=crimson\" \"HAYAT_PWD=hayat_for_all\" \"HAYAT_HOST=web-01.hayat-blood-donation.tech\" \"HAYAT_DB=hayat_prod_db\"
ExecStart=/home/%s/HAYAT/venv/bin/gunicorn -b 0.0.0.0:8000 -w 3 app:app
Restart=always
StandardOutput=file:/var/log/HAYAT/HAYAT-web.out.log
StandardError=file:/var/log/HAYAT/HAYAT-web.err.log

[Install]
WantedBy=multi-user.target
" "$(whoami)" "$(whoami)" "$(whoami)" | sudo tee /etc/systemd/system/HAYAT-web.service >/dev/null

printf "[Unit]
Description=HAYAT API
After=network.target

[Service]
User=%s
Group=%s
WorkingDirectory=/home/youssef/HAYAT/
Environment=\"HAYAT_USER=crimson\" \"HAYAT_PWD=hayat_for_all\" \"HAYAT_HOST=web-01.hayat-blood-donation.tech\" \"HAYAT_DB=hayat_prod_db\"
ExecStart=/home/%s/HAYAT/venv/bin/gunicorn -b 0.0.0.0:8001 -w 3 api.app:app
Restart=always
StandardOutput=file:/var/log/HAYAT/HAYAT-api.out.log
StandardError=file:/var/log/HAYAT/HAYAT-api.err.log

[Install]
WantedBy=multi-user.target
" "$(whoami)" "$(whoami)" "$(whoami)" | sudo tee /etc/systemd/system/HAYAT-API.service >/dev/null

sudo systemctl daemon-reload
sudo systemctl restart HAYAT-web
sudo systemctl restart HAYAT-API
sudo systemctl enable HAYAT-web
sudo systemctl enable HAYAT-API
