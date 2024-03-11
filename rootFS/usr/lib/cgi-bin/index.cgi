#!/bin/bash
IP=`hostname -I`
NETNAME=`hostname -s`
CLOCKFACE=`date`
KERNEL=`uname -a`
TEMP=`cat /var/www/html/cgi-bin/temp`
RUNNINGTIME=`uptime`
EXCITER=`cat /var/www/html/cgi-bin/catfiles/components/Exciter/power`
PLL=`cat /var/www/html/cgi-bin/catfiles/components/Exciter/pll`
AMP=`cat /var/www/html/cgi-bin/catfiles/components/Amplifier/status`
TXPWR=`cat /var/www/html/cgi-bin/catfiles/components/Amplifier/drive`
AUDSRC=`cat /var/www/html/cgi-bin/catfiles/components/Audio/clipper.source`
MPXCLIP=`cat /var/www/html/cgi-bin/catfiles/components/Audio/clipper.status`
ALERTMAIL=`cat /var/www/html/cgi-bin/catfiles/Numerics/alertmail`

echo "content-type: text/plain"
echo
echo  "Network Address (IPv4):"
echo  "$IP"
echo  
echo  "Network Name:"
echo  "$NETNAME"
echo
echo  "Current Time:"
echo  "$CLOCKFACE"
echo
echo  "System Info:"
echo  "$KERNEL"
echo
echo  "CPU Temperature:"
echo  "$TEMP"
echo
echo  "Uptime:"
echo  "$RUNNINGTIME"
echo
echo  "Exciter Status:"
echo  "$EXCITER"
echo
echo  "PLL Status:"
echo  "$PLL"
echo
echo  "Amplifier Status:"
echo  "$AMP"
echo
echo  "Amplifier Drive:"
echo  "$TXPWR"
echo
echo  "Audio Source:"
echo  "$AUDSRC"
echo
echo  "ALERT STATUS:"
echo  "$ALERTMAIL"
echo
echo "More Statistics on next page..."
