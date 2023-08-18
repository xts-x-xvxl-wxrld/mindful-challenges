#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

while :; do sleep 6h & wait $${!}; nginx -s reload; done & nginx -g \"daemon off;\"
