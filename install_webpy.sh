#!/usr/bin/env bash

function install_webpy
{
    local pkg_dir=/data/git/podm/tools/setup/rpms/
    local pkg_file=$(ls $pkg_dir | grep web.py)
    local easy_tool=$(which easy_install)
    if [[ -n $easy_tool ]];then
        $easy_tool $pkg_dir$pkg_file
    else
        local pip_tool=$(which pip)
        [[ $? -eq 0 ]] || (echo "one two three...";exit)
        #echo "neither easy_install or pip tool available, skip webpy installation, but this will lead to unavailable service of podm-demo"
        $pip_tool install $pkg_dir$pkg_file
    fi
}

install_webpy
