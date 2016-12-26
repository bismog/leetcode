#!/usr/bin/env bash

pip_config="~/.xxx/xxx.conf"
echo "Create $pip_config ..."
if [ ! -d `dirname $pip_config` ]; then
    mkdir -p `dirname $pip_config`
fi
