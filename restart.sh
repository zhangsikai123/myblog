#!/bin/bash
echo app restart ...

./rebuild.sh

docker-compose up
