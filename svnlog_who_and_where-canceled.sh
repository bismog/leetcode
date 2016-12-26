#!/usr/bin/env bash


branch_list="http://10.43.25.237/svn/ZXV4PF/branches http://10.43.25.237/svn/ZX3GPF/branches/ZX3GPF_V05.03.83/code"

user_list="10033363 10112914"
#grep_user_list=echo $user_list | awk 'BEGIN {OFS='\|'} {print $0}'
#grep_user_list=`echo $user_list | awk 'BEGIN {OFS="\\|"} {sep=""; for (i=1; i<=NF; i++) {printf("%s%s",sep,$i); sep=OFS}; printf("\n")}'`
grep_user_list=`echo $user_list | awk 'BEGIN {OFS="\\|"} {sep=""; for (i=1; i<=NF; i++) {printf("%s%s",sep,$i); sep=OFS}}'`
echo $grep_user_list
#local log_filter_out=$(mktemp)
local log_filter_out=/tmp/svnlogxxx.out

log_filter()
{
    svn log $1 | grep '10033363\|10112914' > $log_filter_out
}

for branch in $branch_list
do
    log_filter $branch
done
