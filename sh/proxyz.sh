#!/usr/bin/env bash

proxy_config_file=/etc/profile
# docker_environ_file=/etc/systemd/system/docker.service.d/http-proxy.conf
# docker_config_file=/etc/sysconfig/docker

if [[ $1 == "0" ]];then
    sed -i '/http_proxy/s/export/#export/' $proxy_config_file
    sed -i '/https_proxy/s/export/#export/' $proxy_config_file
    sed -i '/ftp_proxy/s/export/#export/' $proxy_config_file
    sed -i '/socks_proxy/s/export/#export/' $proxy_config_file
    sed -i '/all_proxy/s/export/#export/' $proxy_config_file
    sed -i '/no_proxy/s/export/#export/' $proxy_config_file
    export http_proxy=
    export https_proxy=
elif [[ $1 == "1" ]];then
    sed -i '/http_proxy/s/#*export/export/' $proxy_config_file 
    sed -i '/https_proxy/s/#*export/export/' $proxy_config_file
    sed -i '/ftp_proxy/s/#*export/export/' $proxy_config_file  
    sed -i '/socks_proxy/s/#*export/export/' $proxy_config_file
    sed -i '/all_proxy/s/#*export/export/' $proxy_config_file  
    sed -i '/no_proxy/s/#*export/export/' $proxy_config_file    
else
    first_two_segment=`echo $1 | awk 'BEGIN{FS=OFS="."} {print $1,$2}'`
    if [[ $first_two_segment == "10.43" ]];then
        sed -i '/springboard=/c\export springboard='"${1}"'' $proxy_config_file
        sed -i '/http_proxy/s/#*export/export/' $proxy_config_file
        sed -i '/https_proxy/s/#*export/export/' $proxy_config_file
        sed -i '/ftp_proxy/s/#*export/export/' $proxy_config_file
        sed -i '/socks_proxy/s/#*export/export/' $proxy_config_file
        sed -i '/all_proxy/s/#*export/export/' $proxy_config_file
        sed -i '/no_proxy/s/#*export/export/' $proxy_config_file

#         sed -i '/HTTP_PROXY/c\export HTTP_PROXY=http://'"${1}"':6464/'  $docker_config_file
#         sed -i '/HTTPS_PROXY/c\export HTTPS_PROXY=https://'"${1}"':6464/'  $docker_config_file
# 
#         sed -i '/Environment=/c\Environment="HTTP_PROXY=http://'"${1}"':6464/"' $docker_environ_file
#         systemctl daemon-reload
#         is_active=$(systemctl is-active docker.service)
#         if [[ is_active == 'active' ]];then
#             systemctl restart docker
#         fi
    fi
fi
source ${proxy_config_file}


