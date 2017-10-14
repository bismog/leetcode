#!/usr/bin/env bash

set -uex

# Assume we have 'mount -B /home/git/projectxxx/code/projectxxx/projectxxx /lib/python2.7/site-packages/projectxxx' 
pushd /home/git/projectxxx
git fetch origin
git reset --hard origin/upstreamfirst
sh ./tools/copy_openstack_code.sh
supervisorctl restart projectxxx-api
projectxxx-manage db_sync
popd
