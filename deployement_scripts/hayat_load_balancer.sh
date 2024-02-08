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
	ip_hash;
        server web-01.hayat-blood-donation.tech;
        server web-02.hayat-blood-donation.tech;
}

server {
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;

        server_name hayat-blood-donation.tech www.hayat-blood-donation.tech;

        ssl_certificate /home/youssef/ssl/hayat-blood-donation_tech_chain.crt;

        ssl_certificate_key /home/youssef/server_keys/server.key;

        location /api {
                proxy_pass http://web-01.hayat-blood-donation.tech;
        }

        location /register {
                proxy_pass http://web-01.hayat-blood-donation.tech;
        }

        location / {
                proxy_pass http://hayat_servers;
        }

        location /static {
                proxy_pass http://hayat_servers;
        }
}

server {
        listen 80;
        listen [::]:80;

        server_name hayat-blood-donation.tech www.hayat-blood-donation.tech;

        return 301 https:/\$server_name\$request_uri;
}
" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

sudo systemctl restart nginx
