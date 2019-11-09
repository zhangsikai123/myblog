#!/bin/bash

docker run -it --network myblog_default --rm mongo mongo --host mongo:27017
