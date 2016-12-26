#!/bin/bash

#command "service ceph status" only show running osd, osd with status down/out will not mention, can use command "ceph osd tree" get osd list instead
osd_list=`service ceph status | grep "===" | awk '{print$2}'`

for osd in $osd_list
do
    #stop osd service
    /etc/init.d/ceph stop $osd
    ceph osd crush rm $osd
    ceph osd rm $osd
    ceph auth del $osd
done

#umount /var/lib/ceph/osd/ceph-xxx
dir_list=`mount | grep osd | awk '{print $3}'`
part_list_reverse=`mount | grep osd | awk '{print $1}' | sort -r`
for dir in $dir_list
do
    umount $dir
done

#parted remove dev
for part in $part_list_reverse
do
    dev_name=`echo $part | tr -d '[:digit:]'`
    part_seq=`echo $part | tr -d '/' | tr -d '[:alpha:]'`
    echo "$dev_name rm $part_seq"
    #parted $dev_name rm $part_seq
done

yum remove -y ceph
