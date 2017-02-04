#!/usr/bin/env python

available_combinations =\
(
("vxlan", "dvs","active-backup", "off"),
("vxlan", "dvs","balance-slb", "off"),
("vxlan", "dvs,sriov","active-backup", "off"),
("vxlan", "dvs,sriov","balance-slb", "off"),
("vxlan", "dvs,sriov","active-backup", "off"),
("vxlan", "dvs,sriov","balance-slb", "off"),
("vxlan", "dvs,sriov","balance-tcp", "active"),
("vxlan", "dvs,sriov","balance-tcp", "passive"),
("vxlan", "dvs,sriov","balance-tcp", "off"),
("vlan", "ovs","active-backup", "off"),
("vlan", "ovs","balance-slb", "off"),
("vlan", "ovs,sriov","active-backup", "off"),
("vlan", "ovs,sriov","balance-slb", "off"),
("vlan", "ovs","balance-tcp", "active"),
("vlan", "ovs","balance-tcp", "passive"),
("vlan", "ovs","balance-tcp", "off"),
("vlan", "ovs,sriov","balance-tcp", "active"),
("vlan", "ovs,sriov","balance-tcp", "passive"),
("vlan", "ovs,sriov","balance-tcp", "off"),
("vlan", "dvs","active-backup", "off"),
("vlan", "dvs","balance-slb", "off"),
("vlan", "dvs,sriov","active-backup", "off"),
("vlan", "dvs,sriov","balance-slb", "off"),
("vlan", "dvs","balance-tcp", "active"),
("vlan", "dvs","balance-tcp", "passive"),
("vlan", "dvs","balance-tcp", "off"),
("vlan", "dvs,sriov","balance-tcp", "active"),
("vlan", "dvs,sriov","balance-tcp", "passive"),
("vlan", "dvs,sriov","balance-tcp", "off"))


def find_data():
    vlan_type = "vxlan"
    vswitch_type = "dvs,sriov" 
    bond_mode = "balance-slb"
    lacp_mode = "off"

    # ttt = tuple([vlan_type, vswitch_type, bond_mode, lacp_mode])
    ttt = (vlan_type, vswitch_type, bond_mode, lacp_mode)

    if ttt in available_combinations:
        print "Yes, it's in"
    else:
        print "No, not found"

if __name__ == "__main__":
    find_data()
