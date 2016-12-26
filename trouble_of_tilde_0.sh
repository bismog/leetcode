#!/usr/bin/env bash

#ppp="~/.xxx/xxxfile"
ppp="/root/.yyy/xxxfile"
sudo rm -rf $ppp
echo "Create $ppp..."
#if [ ! -d `dirname $ppp` ]; then
#    mkdir -p `dirname $ppp`
#fi
sudo cat <<EOF >$ppp
i
like
it
anyway
EOF
ls -l $ppp
