#!/bin/bash
echo app restart ...

./rebuild.sh

nohup docker-compose up &
