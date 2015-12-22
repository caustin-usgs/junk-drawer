#!/bin/bash
iptables -t nat -F
ifconfig docker0 down
brctl delbr docker
docker --dns 8.8.8.8 --dns 8.8.4.4 --dns 152.61.192.1 --dns 136.177.16.3 --dns-search cr.usgs.gov -d



