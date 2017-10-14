#!/bin/bash

#get conf file and keyring from node monitor
#mon_user="root"
#mon_psd="companyxxxscs"
#mon_hostname="cml01"
#scp $mon_user@$mon_hostname:/etc/ceph/ceph.conf /etc/ceph/
#expect "$mon_user@$mon_hostname's password:"
#send "$mon_psd\r"
#
#scp $mon_user@$mon_hostname:/var/lib/ceph/bootstrap-osd/ceph.keyring /var/lib/ceph/bootstrap-osd/
#expect "$mon_user@$mon_hostname's password:"
#send "$mon_psd\r"

#install ceph package
yum install -y ceph

#get cluster-uuid
yum install -y crudini
ceph_uuid=`crudini --get /etc/ceph/ceph.conf global fsid`


#parted /dev/sda mkpart logical xfs "23.8G" "131G"
#parted /dev/sda mkpart logical xfs "131G" "231G"
#parted /dev/sda mkpart logical xfs "231G" "318G"
mkdir -p /var/lib/ceph/osd
ceph-disk prepare --cluster ceph --cluster-uuid $ceph_uuid --fs-type xfs /dev/sda5
ceph-disk prepare --cluster ceph --cluster-uuid $ceph_uuid --fs-type xfs /dev/sda6
ceph-disk prepare --cluster ceph --cluster-uuid $ceph_uuid --fs-type xfs /dev/sda7
ceph-disk activate /dev/sda5
ceph-disk activate /dev/sda6
ceph-disk activate /dev/sda7
