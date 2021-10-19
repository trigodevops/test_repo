#!/bin/sh
# vim:sw=4:ts=4:et

set -e

nohup mosquitto_sub -h mosquitto-a -v -t 'trigo/#' >> /usr/share/nginx/html/config &
