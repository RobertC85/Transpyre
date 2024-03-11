#!/bin/bash
NET=`ifconfig`
echo "content-type: text/plain"
echo
echo  "Basic Network Settings:" 
echo  "$NET"
