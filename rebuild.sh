#!/bin/bash


echo git pull ...
git pull


echo app rebuild ...

app_image=skyblogger

nginx_image=skyblogger-nginx


docker build . -f Dockerfile-app -t $app_image
docker build . -f Dockerfile-nginx -t $nginx_image
