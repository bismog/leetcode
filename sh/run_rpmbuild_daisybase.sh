#!/usr/bin/env bash

# source image file should be restricted to name:
# daisy-base.tar.gz, $1 could be a full-path name
sourceimg=$1
if [[ $1 == "" ]];then
    sourceimg=./daisy-base.tar.gz
fi

anchor="daisy-base-1.0.0"
tmpdir=$(mktemp -d)
mkdir -p $tmpdir/$anchor
cp $sourceimg $tmpdir/$anchor/
cd $tmpdir/
tar -czvf $anchor.tar.gz -C $tmpdir $anchor
mv $anchor.tar.gz /root/rpmbuild/SOURCES/
cd /root/rpmbuild/SPECS/

# please run this script below /root/rpmbuild/SPECS
rpmbuild -bb --define '_arch x86_64' --define '_topdir /root/rpmbuild' --define '_version 1.0.0' daisy-base.spec
