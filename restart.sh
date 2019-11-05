#!/bin/bash
echo app restart ...

docker-compose stop

app_image=skyblogger
nginx_image=skyblogger-nginx

docker build . -f Dockerfile-app -t $app_image
docker build . -f Dockerfile-nginx -t $nginx_image

nohup docker-compose up >> logs/docker-compose.log &
