#!/usr/bin/env bash

pip_config="/root/.pip/pip.conf"
repos_ip=10.43.177.160
sudo rm -rf $pip_config
echo "Create $pip_config ..."
if [ ! -d `dirname $pip_config` ]; then
    mkdir -p `dirname $pip_config`
fi
sudo cat <<EOF >$pip_config
[global]
trusted-host = $repos_ip
find-links = http://$repos_ip/pypi
no-index = true
EOF
ls -l $pip_config
