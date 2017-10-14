#!/usr/bin/env bash
# -*- coding:utf-8 -*-

projectxxx_TREE_ROOT=/home/git/projectxxx

# Assume we have setup git working tree in /home/git/projectxxx
# and mounting is ready.
pushd $projectxxx_TREE_ROOT
git fetch origin
git reset --hard origin/upstreamfirst

# project0xxx/projectxxx branch upstreamfirst has a weird trick by putting some code to a
# special direcotry 'upstream', so we must run a copy-to-dest script before
# run them.
pushd ${projectxxx_TREE_ROOT}/tools
sh copy_openstack_code.sh
popd
git add .
# How to commit non-interactively?
git commit --amend -m 'copy_code'
popd

# Synchronize projectxxx database
projectxxx-manage db_sync

# Now you can do 'git merge' or 'git cherry-pick' or 'alter and git add git
# commit' to adjust your code. After all these done, just restart related
# services.
supervisorctl restart all
supervisorctl status
