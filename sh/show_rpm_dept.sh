#!/usr/bin/env bash

outfile=depts.all
rm -rf $outfile
for pkg in `ls`; do
    dept_rpms=`rpm -qpR $pkg`
    echo >> $outfile
    echo "rpm $pkg depent on:" >> $outfile
    echo $dept_rpms >> $outfile
done
    
