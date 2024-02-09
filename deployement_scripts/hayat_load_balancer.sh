#!/usr/bin/env bash
# Set HAProxy load balancer for HAYAT website

last_update=$(stat -c %Y /var/lib/apt/periodic/update-success-stamp 2>/dev/null || stat -c %Y /var/cache/apt/pkgcache.bin 2>/dev/null)

current_time=$(date +%s)
update_threshold=$((24 * 60 * 60))  # 24 hours in seconds

if [ "$((current_time - last_update))" -gt "$update_threshold" ]; then
    sudo apt update
fi
# Install HAProxy from PPA repository
if ! dpkg -l | grep -q haproxy; then
    sudo add-apt-repository ppa:vbernat/haproxy-2.6 -y
    sudo apt update
    sudo apt install haproxy=2.6.* -y
fi

# Create a backup of the original HAProxy configuration file
sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bk

# Write the new HAProxy configuration file
printf "# Load balancer configuration for HAYAT website

frontend http_front
    bind *:80
    bind *:443 ssl crt /home/youssef/ssl/hayat-blood-donation_tech_chain.crt
    redirect scheme https code 301 if ! { ssl_fc } # Redirect HTTP to HTTPS
    default_backend http_back

backend http_back
    balance roundrobin
    cookie SERVERID insert indirect nocache
    server web-01 web-01.hayat-blood-donation.tech:80 check cookie web-01
    server web-02 web-02.hayat-blood-donation.tech:80 check cookie web-02
" | sudo tee /etc/haproxy/haproxy.cfg >/dev/null

# Restart HAProxy service
sudo systemctl restart haproxy
