#!/bin/bash
docker build --pull -t blink:latest -f docker/Dockerfile . 
docker run -e LOG_FILE="/home/logs/blink_led.log" \
           -e LOGLEVEL="info" \
           -e LEDPIN=8 \
           -e INTERVAL=1 \
           -v /home/lucas/projects/container-gpio/logs:/home/logs \
           --device /dev/gpiomem \
           blink
