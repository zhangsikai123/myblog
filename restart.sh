#!/bin/bash
echo app restart ...

./rebuild.sh

docker-compose down

nohup docker-compose up &
