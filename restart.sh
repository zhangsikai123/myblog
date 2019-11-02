#!/bin/bash
echo app restart ...
image=skyblogger
docker stop $(docker ps -q --filter ancestor=$image)
docker build . -t $image
docker run --net=host $image
