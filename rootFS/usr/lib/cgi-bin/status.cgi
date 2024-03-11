#!/bin/bash
DEVMESG=`cat /home/dietpi/devmesg.txt`

echo "content-type: text/plain"
echo
echo  "Transmitter overall status:"
echo  "$HEALTH"
echo
echo  "Please select one of the submenu options to the left for more information!"
echo  "Overview shows the most basic stats such as network configuration, broadcast status and more."
echo  "Alerts are warnings from the system, you will automatically see an indicator of how many alerts exist under status > overview."
echo  "The section titled Amplification will display advanced statistics about your transmitter's power output."
echo  "The Audio section of the status menu displays current audio source, composite clipper settings and more."
echo  "Automation deals with function scheduling ans is not yet implemented at all."
echo  "The Electrical submenu is a series of advanced safety features."
echo  "Health includes such information as signal quality and hardwre health information."
echo  "Networking includes information about this transmitter's network identity and where to get backup audio from."
echo  "Options shows you all that you can do right now."
echo
echo
echo
echo "      Other menu options include audio settings such as Multiplex source and composite clipping, Radio Frequency or simply RF allows you to configure signal strength and Utility provides more options for both transmitter and onboard computer"
echo
echo
echo
echo  "Messsages from TransPyre Developer Robert Cotterman will appear below."
echo
echo  "$DEVMESG"
