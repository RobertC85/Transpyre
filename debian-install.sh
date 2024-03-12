#!/bin/sh
echo "Not Ready Yet, this will be a public open source project soon, but for the love of your sanity please press ctrl+c now!"
sleep 15
#installing dependencies
sudo apt install -y x11vnc xorg xinit chromium-browser apache2 proftpd vlc npm nodejs
echo "okay i got that part, this is the last step before we start making real changes and installing our software to your device, i'll give you a few seconds to change your mind"
sleep 5
echo "okay you glutton for punishment by pre-alpha software testing you, here we go"
sudo cp -r ~/transpyre/rootFS/* /
sudo a2enmod cgid
echo "ok if we are still alive you can login with your browser to your devices IP to access your options, i'm going to add VNC here in a moment"
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "@reboot /usr/local/sbin/.vnclauncher" >> mycron
echo "@reboot /usr/local/sbin/startup" >> mycron
echo "* * * * * /var/www/html/cgi-bin/temp.sh" >> mycron
#install new cron file
crontab mycron
rm mycron
sudo service apache2 restart
#INSTALLING CRONICLE SCHEDULE MANAGER
mkdir -p /opt/cronicle
cd /opt/cronicle
curl -L https://github.com/jhuckaby/Cronicle/archive/v1.0.0.tar.gz | tar zxvf - --strip-components 1
npm install
node bin/build.js dist
# CRONICLE IS MIT LICENSED SO SHOULD BE ABLE TO BE ADDED HERE.
