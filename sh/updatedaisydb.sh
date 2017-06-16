#!/usr/bin/env bash

set -uex

# Assume we have 'mount -B /home/git/daisy/code/daisy/daisy /lib/python2.7/site-packages/daisy' 
pushd /home/git/daisy
git fetch origin
git reset --hard origin/upstreamfirst
sh ./tools/copy_openstack_code.sh
supervisorctl restart daisy-api
daisy-manage db_sync
popd
