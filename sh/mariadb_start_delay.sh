#!/usr/bin/env bash

# Assume you have disable mariadb.service before run this test script

function clean_mysql
{
    mysql <<EOF
drop database if exists xxx;
drop database if exists yyy;
drop database if exists zzz;
exit
EOF
}

function create_database
{
    mysql <<EOF
create database if not exists xxx;
create database if not exists yyy;
create database if not exists zzz;
exit
EOF
}

while true;do
    # systemctl stop mariadb
    sleep 5
# run clean_mysql and then start mariadb to find if mariadb.service 
# start failed for the attemped connection
    systemctl start mariadb
    # no wait
    clean_mysql
    sleep 5
    ## systemctl is-active mariadb
    if systemctl is-active mariadb;then
        create_database
    fi
    systemctl stop mariadb
    sleep 10
done

