#!/usr/bin/env bash
# -*- coding:utf-8 -*-

# In order to build code environment in projectxxx container, we would have to 
# prepare some tools such as git, git-review(optional)

# update /etc/hosts, append following domain name:
# gerrit.companyxxx.com.cn     (mandatory)
# mirrors.companyxxx.com.cn    (mandatory)
# artifacts.companyxxx.com.cn  (optional)
cat <<EOF >> /etc/hosts
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
curl -o /etc/yum.repos.d/contrib_projectxxx.repo http://10.43.211.64/repofile/contrib_projectxxx.repo

yum install --disablerepo=* --enablerepo=centos7 -y git
yum install --disablerepo=* --enablerepo=contrib_projectxxx -y python-pip

mkdir -p /root/.pip
cat <<EOF > /root/.pip/pip.conf
[global]
index-url = http://mirrors.companyxxx.com.cn/pypi/simple
trusted-host = mirrors.companyxxx.com.cn
format=legacy
EOF
pip install git-review

# 
rm -f /etc/yum.repos.d/centos7.repo
rm -f /etc/yum.repos.d/contrib_projectxxx.repo
# rm -f /etc/yum.repos.d/contrib_project0xxx.repo
# for repo in $(ls -1 /etc/yum.repos.d)
# do
#     # remove right part after last '.' character
#     mv ${repo} ${repo}.xxx
# done

# Now you should manually upload public key in container to gerrit server
while true; do
    read -p "Have you upload public key?" yes_or_no
    case $yes_or_no in
        [Yy]* ) break;;
        [Nn]* ) ;;
        * ) echo "Please answer yes or no.";;
    esac
done

mkdir -p /home/git/
cd /home/git/
# Here please replace 'workidxxx' to your id
git clone --branch upstreamfirst --single-branch ssh://workidxxx@gerrit.companyxxx.com.cn:29418/project0xxx/projectxxx
cd projectxxx
# Here please replace 'cml' to your real name
git config user.name cml
# Here please replace 'c.ml@companyxxx.com.cn' to your real email
git config user.email c.ml@companyxxx.com.cn

# project0xxx/projectxxx branch upstreamfirst has a weird trick by putting some code to a 
# special direcotry 'upstream', so we must run a copy-to-dest script before
# run them.
pushd tools
sh copy_openstack_code.sh
popd
git add .
git commit -m 'copy_code'

# create .gitreview for 'git review ...' command
cat <<EOF > .gitreview
[gerrit]
host=gerrit.companyxxx.com.cn
port=29418
project=project0xxx/projectxxx
defaultbranch=upstreamfirst
defaultremote=origin
defaultrebase=0
EOF

# Mount source code with bind mode to real directory while service running
mount -B code/projectxxx/projectxxx /lib/python2.7/site-packages/projectxxx
mount -B code/projectxxxclient/projectxxxclient /lib/python2.7/site-packages/projectxxxclient
mount -B code/horizon/openstack_dashboard/dashboards /usr/share/openstack-dashboard/openstack_dashboard/dashboards
mount -B code/horizon/openstack_dashboard/locale /usr/share/openstack-dashboard/openstack_dashboard/locale
mount -B code/horizon/openstack_dashboard/api /usr/share/openstack-dashboard/openstack_dashboard/api

# Synchronize projectxxx database
projectxxx-manage db_sync

# Now you can do 'git merge' or 'git cherry-pick' or 'alter and git add git 
# commit' to adjust your code. After all these done, just restart related 
# services.
supervisorctl restart all
