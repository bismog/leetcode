#!/bin/bash
#install ceph package
yum install -y ceph

#config ceph conf file
ceph_conf_file="/etc/ceph/ceph.conf"
(\
echo "[global]";\
echo "fsid = ";\
echo "mon initial members = ";\
echo "mon host = ";\
echo "public network = ";\
echo "auth cluster required = cephx";\
echo "auth service required = cephx";\
echo "auth client required = cephx";\
echo "osd journal size = 1024";\
echo "filestore xattr use omap = true";\
echo "osd pool default size = 2";\
echo "osd pool default min size = 1";\
echo "osd pool default pg num = 128";\
echo "osd pool default pgp num = 128";\
echo "osd crush chooseleaf type = 1";\
)>$ceph_conf_file

#replace /etc/ceph/ceph.conf
ceph_uuid=`uuidgen`
mon_name=`hostname -s`
#mon_ip="10.43.167.19"
mon_ip=`hostname -i`
public_network="10.43.167.0/24"
sed -i "/fsid/cfsid = $ceph_uuid" $ceph_conf_file
sed -i "/mon initial members/cmon initial members = $mon_name" $ceph_conf_file
sed -i "/mon host/cmon host = $mon_ip" $ceph_conf_file
sed -i "/public network/cpublic network = $public_network" $ceph_conf_file

#generate keyring for monitor(mon.) and administrator(client.admin)
ceph-authtool --create-keyring /tmp/ceph.mon.keyring --gen-key -n mon. --cap mon 'allow *'
#ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --set-uid=0 --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow'
ceph-authtool --create-keyring /etc/ceph/ceph.client.admin.keyring --gen-key -n client.admin --set-uid=0 --cap mon 'allow *' --cap osd 'allow *' --cap mds 'allow *'
ceph-authtool /tmp/ceph.mon.keyring --import-keyring /etc/ceph/ceph.client.admin.keyring
#generate monitor map
monmaptool --create --add $mon_name $mon_ip --fsid $ceph_uuid /tmp/monmap
mkdir -p /var/lib/ceph/mon/ceph-$mon_name
#populate monitor daemon with map and keyring
ceph-mon --mkfs -i $mon_name --monmap /tmp/monmap --keyring /tmp/ceph.mon.keyring
#tourch the done file
touch /var/lib/ceph/mon/ceph-$mon_name/done
touch /var/lib/ceph/mon/ceph-$mon_name/sysvinit
#cmladd, copy keyring to /var/lib/ceph/mon/ceph-xxx/
cp /tmp/ceph.mon.keyring /var/lib/ceph/mon/ceph-$mon_name/keyring
#start monitor
/etc/init.d/ceph start mon.$mon_name

