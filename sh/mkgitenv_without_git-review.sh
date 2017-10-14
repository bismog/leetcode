#!/usr/bin/env bash
# -*- coding:utf-8 -*-

# In order to build code environment in projectxxx container, we would have to 
# prepare some tools such as git, git-review(optional)

# update /etc/hosts, append following domain name:
# gerrit.companyxxx.com.cn     (mandatory)
# gerritro.companyxxx.com.cn   (optional)
# mirrors.companyxxx.com.cn    (mandatory)
# artifacts.companyxxx.com.cn  (optional)
echo <<EOF > /etc/hosts
10.31.48.30     mirrors.companyxxx.com.cn
10.41.103.20    gerrit.companyxxx.com.cn
10.31.48.42     artifacts.companyxxx.com.cn
EOF

# for repo in $(ls -1 /etc/yum.repos.d)
# do
#     mv ${repo} ${repo}.xxx
# done
# scp root@10.43.174.101:/etc/yum.repos.d/centos7.repo /etc/yum.repos.d/
# scp root@10.43.174.101:/etc/yum.repos.d/contrib_projectxxx.repo /etc/yum.repos.d/
# scp root@10.43.174.101:/etc/yum.repos.d/contrib_project0xxx.repo /etc/yum.repos.d/
curl -o /etc/yum.repos.d/centos7.repo http://10.43.211.64/repofile/centos7.repo

yum install --disablerepo=* --enablerepo=centos7 -y git

rm -f /etc/yum.repos.d/centos7.repo
# rm -f /etc/yum.repos.d/contrib_projectxxx.repo
# rm -f /etc/yum.repos.d/contrib_project0xxx.repo
# for repo in $(ls -1 /etc/yum.repos.d)
# do
#     # remove right part after last '.' character
#     mv ${repo} ${repo}.xxx
# done

mkdir -p /home/git/
cd /home/git/
git clone --branch upstreamfirst --single-branch ssh://xxxxxxxx@gerrit.companyxxx.com.cn:29418/project0xxx/projectxxx
cd projectxxx
git config user.name yourname
git config user.email your.name@companyxxx.com.cn

# project0xxx/projectxxx branch upstreamfirst has a weird trick by putting some code to a 
# special direcotry 'upstream', so we must run a copy-to-dest script before
# run them.
pushd tools
sh copy_openstack_code.sh
popd
git add .
git commit -m 'copy_code'

# Without git-review, we can cherry-pick pending review code as follow:
# Find pending review that you want cherry-pick from, for examle:
# Gerrit change number: 13579
# Patch-set number: 3
# Your ID of companyxxx: 10099999
# Just run:
# git fetch ssh://10099999@gerrit.companyxxx.com.cn:29418/project0xxx/projectxxx refs/changes/79/13579/3 && git cherry-pick FETCH_HEAD

# Mount source code with bind mode to real directory while service running
mount -B code/projectxxx/projectxxx /lib/python2.7/site-packages/projectxxx
mount -B code/projectxxxclient/projectxxxclient /lib/python2.7/site-packages/projectxxxclient
mount -B code/horizon/openstack_dashboard/dashboards /usr/share/openstack-dashboard/openstack_dashboard/dashboards
mount -B code/horizon/openstack_dashboard/locale /usr/share/openstack-dashboard/openstack_dashboard/locale
mount -B code/horizon/openstack_dashboard/api /usr/share/openstack-dashboard/openstack_dashboard/api

# Now you can do 'git merge' or 'git cherry-pick' or 'alter and git add git 
# commit' to adjust your code. After all these done, just restart related 
# services.
# supservisorctl restart all
