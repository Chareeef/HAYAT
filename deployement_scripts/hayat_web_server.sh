#!/usr/bin/env bash
# Deploy HAYAT website through nginx web server

last_update=$(stat -c %Y /var/lib/apt/periodic/update-success-stamp 2>/dev/null || stat -c %Y /var/cache/apt/pkgcache.bin 2>/dev/null)

current_time=$(date +%s)
update_threshold=$((24 * 60 * 60))  # 24 hours in seconds

if [ "$((current_time - last_update))" -gt "$update_threshold" ]; then
    sudo apt update
fi

if ! dpkg -l | grep -q nginx; then
    sudo apt install nginx -y
fi

printf "# Server block for HAYAT website

server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name %s;

	add_header ServedBy %s;

	location / {
		proxy_pass http://localhost:8000;
	}

	location /static {
		proxy_pass http://localhost:8000;
	}

	location /api {
		proxy_pass http://localhost:8001;
	}
}
" "$(hostname)" "$(hostname)" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

sudo systemctl restart nginx
