#!/bin/bash

wai=`whoami`
if [[ $wai != 'root' ]]
  then
    echo 'this script needs to be run as root'
    exit 2
fi

echo 'this script is for a very specific use case. 
Windows 7, running an Ubuntu 15.10 VirtualBox 
instance, in order to allow Docker
containers to connect to the interwebs'

ip1='152.61.192.1'
ip2='136.177.16.3'
restart=False

cd /etc
for ip in $ip1 $ip2
  do
    if [[ -z `grep ${ip} resolv.conf` ]]
      then
        echo "nameserver $ip" >> resolv.conf
        restart=True
    fi
done

docker_settings='/etc/default/docker'
if [[ ! -z `grep ^D $docker_settings` ]]
then
  echo "all lines need to be commented out in ${docker_settings}"
  echo "commenting them out now..."
  sed -i "s/^D/#D/g" $docker_settings
  echo " done "
fi

if [[ $restart == True ]]
  then
    echo "restart docker:  service docker restart ..."
    service docker restart
fi
