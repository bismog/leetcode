#!/usr/bin/env bash
# -*- coding:utf-8 -*-

DAISY_TREE_ROOT=/home/git/daisy

# Assume we have setup git working tree in /home/git/daisy
# and mounting is ready.
pushd $DAISY_TREE_ROOT
git fetch origin
git reset --hard origin/upstreamfirst

# tecs/daisy branch upstreamfirst has a weird trick by putting some code to a
# special direcotry 'upstream', so we must run a copy-to-dest script before
# run them.
pushd ${DAISY_TREE_ROOT}/tools
sh copy_openstack_code.sh
popd
git add .
# How to commit non-interactively?
git commit --amend -m 'copy_code'
popd

# Synchronize daisy database
daisy-manage db_sync

# Now you can do 'git merge' or 'git cherry-pick' or 'alter and git add git
# commit' to adjust your code. After all these done, just restart related
# services.
supervisorctl restart all
supervisorctl status
