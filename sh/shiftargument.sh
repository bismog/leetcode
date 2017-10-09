#!/usr/bin/env bash

index=1
while (( $# )); do
    echo "The $index argument is: $1"
    let index+=1
    shift
done
