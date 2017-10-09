#!/usr/bin/env bash
#-*- coding:utf-8 -*-

stuff=$1
base_dir=$(dirname ${stuff})
prefix=$(echo ${base_dir} | awk -F '/' '{print $1}')
# Just copy if given full path file
if [ "$prefix" == "" ];then
    rsync -r ${stuff} root@10.43.174.101:/home/swapzone/
else
    rsync -r /cygdrive/e/swapzone/${stuff} root@10.43.174.101:/home/swapzone/
fi
echo "Done!"
