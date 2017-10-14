#!/usr/bin/env bash

# version 1
## function match_ip()
## {
##     local ips=$1
##     local target_ip=$2
## 
##     # echo ips are $ips
##     for ip in $ips;do
##         # echo ip is $ip
##         if [[ $target_ip == $ip ]];then
##             echo "Match ok"
##             return 0
##         fi
##     done
##     return 1
## }
## 
## ips=".companyxxx.com.cn,127.0.0.1,10.20.30.40,110.20.30.40,10.11.12.13,110.11.12.133"
## ip_list=$(echo $ips| tr "," " ")
## dest_ip="10.11.12.13"
## match_ip "$ip_list" $dest_ip
## if [[ $? -eq 0 ]];then
##     echo "Congratulations, \"$ip_list\" contain \"$dest_ip\""
## else
##     echo "Sorry, not found \"$dest_ip\" in \"$ip_list\""
## fi

# version 2
ips=".companyxxx.com.cn,127.0.0.1,10.20.30.40,110.20.30.40,10.11.12.13,110.11.12.133"
dest_ip="10.11.12.13"
for ip in $(echo $ips | tr "," " ");do
    if [[ $dest_ip == $ip ]];then
        echo "Congratulations, \"$ips\" contain \"$dest_ip\""
    fi
done
