#!/usr/bin/env bash

path=$1

which yapf 1>/dev/null 2>&1
#[ $? -eq 0 ] && yapf -i $path
if [[ $? -eq 0 ]];then
    yapf -i $path
else
    echo "no yapf found"
fi

which autopep8 1>/dev/null 2>&1
if [[ $? -eq 0 ]];then
    autopep8 -i $path
else
    echo "no autopep8 found"
fi

which isort 1>/dev/null 2>&1
if [[ $? -eq 0 ]];then
    isort $path
else
    echo "no isort found"
fi

