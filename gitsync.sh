#!/usr/bin/env bash

timestamp()
{
    date --rfc-3339=seconds
}

cd /data/git/podm/
# Sync from gerrit(origin/master) to gitlab(http://10.43.211.64:9999/pampas/podmanager master)
timestamp
git push -v gitlab refs/remotes/origin/master:refs/heads/master
