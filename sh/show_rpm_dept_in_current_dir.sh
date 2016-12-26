#!/usr/bin/env bash

outfile=depts.list
rm -rf $outfile
for pkg in `ls`; do
    dept_rpms=`rpm -qpR $pkg | awk '{print $1}'`
    is_first_for_cur_pkg=1
    for dept_rpm in $dept_rpms; do
        ls | grep $dept_rpm >/dev/null 2>&1
        if [ $? -eq 0 ]; then
            if [ $is_first_for_cur_pkg -eq 1 ]; then
                echo >> $outfile
	        echo "rpm $pkg depent on:" >> $outfile
                echo $dept_rpm >> $outfile
                is_first_for_cur_pkg=0
            else
                echo $dept_rpm >> $outfile
            fi
        fi
    done
done
    
