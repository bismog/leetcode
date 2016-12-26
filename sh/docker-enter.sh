#!/usr/bin/env bash

PID=$(docker inspect -f '{{.State.Pid}}' $1)
nsenter -m -u -n -i -p -t $PID
