#!/bin/bash
echo app restart ...

# rebuild all image
./rebuild.sh

docker-compose down

nohup docker-compose up &
