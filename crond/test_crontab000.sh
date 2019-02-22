#!/usr/bin/env bash

label=$1
timestamp=$(date +%Y-%m-%d-%H-%M)
log_file="/run/${timestamp}_${label}"

echo "start..."
> $log_file
echo "...end!"
