#!/bin/sh

while getopts :ab:c opt
do
    case "$opt" in
    a) echo "found -a option";;
    b) echo "found -b option with param $OPTARG";;
    c) echo "found -c option";;
    *) echo "unknown option -$opt";;
    esac
done
shift $[ $OPTIND-1 ]

count=1
for param in "$@"
do
    echo "param $count = $param"
    count=$[ $count+1 ]
done
