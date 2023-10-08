#!/usr/bin/env bash
#

if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
        sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

cat <<EOL >> /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Hello jawad
  </body>
</html>
EOL


sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

text=" \\
\tlocation /hbnb_static {\\
\t\talias /data/web_static/current/;\\
\t}"

_find="location /hbnb_static {"
if ! grep -q -F "$_find" "/etc/nginx/sites-available/default";then
	sudo sed -i "/server_name _;/a $text" /etc/nginx/sites-enabled/default
fi

sudo service nginx restart
