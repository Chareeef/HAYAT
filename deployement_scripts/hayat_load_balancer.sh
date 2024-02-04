#!/usr/bin/env bash
# Set Nginx load balancer for HAYAT website

last_update=$(stat -c %Y /var/lib/apt/periodic/update-success-stamp 2>/dev/null || stat -c %Y /var/cache/apt/pkgcache.bin 2>/dev/null)

current_time=$(date +%s)
update_threshold=$((24 * 60 * 60))  # 24 hours in seconds

if [ "$((current_time - last_update))" -gt "$update_threshold" ]; then
    sudo apt update
fi

if ! dpkg -l | grep -q nginx; then
    sudo apt install nginx -y
fi

printf "# Load balancer configuration for HAYAT website

upstream hayat_servers {
	server web-01.hayat-blood-donation.tech;
	server web-02.hayat-blood-donation.tech;
}

server {
	listen 80 default_server;
	listen [::]:80 default_server;

	server_name _;

	location / {
		proxy_pass http://hayat_servers;
	}
}
" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

sudo systemctl restart nginx
