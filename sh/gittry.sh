#!/usr/bin/env bash
if ! rpm -q git; then yum install -y git; fi
useradd gitt; echo "gitt:gitt" | chpasswd
sed -i '/gitt/s/bash/git-shell/' /etc/passwd
mkdir {gitp,gitc}
cd gitp; git init --bare tryit.git; chown -R gitt:gitt tryit.git; cd -
# Make sure sshd service is running before following scripts
cd gitc; git clone gitt@localhost:$(dirname $(pwd))/gitp/tryit.git

