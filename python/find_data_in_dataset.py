#!/usr/bin/env python

available_combinations = [{
    "vlan_type": "vxlan",
    "vswitch_type": ["dvs"],
    "bond_mode": ['active-backup', 'balance-slb'],
    "lacp_mode": ["off"]
},
{
    "vlan_type": "vxlan",
    "vswitch_type": ["dvs", "dvs,sriov"],
    "bond_mode": ['active-backup', 'balance-slb'],
    "lacp_mode": ["off"]
},
{
    "vlan_type": "vxlan",
    "vswitch_type": ["dvs", "dvs,sriov"],
    "bond_mode": ['balance-tcp'],
    "lacp_mode": ["active", "passive", "off"]
},
{
    "vlan_type": "vlan",
    "vswitch_type": "dvs",
    "bond_mode": "balance-tcp",
    "lacp_mode": "passive"
},
{
    "vlan_type": "vxlan",
    "vswitch_type": "dvs",
    "bond_mode": "balance-tcp",
    "lacp_mode": "passive"
},
{
    "vlan_type": "vlan",
    "vswitch_type": ["ovs", "ovs,sriov"],
    "bond_mode": ['active-backup', 'balance-slb'],
    "lacp_mode": ["off"]
},
{
    "vlan_type": "vlan",
    "vswitch_type": ["ovs", "dvs,sriov"],
    "bond_mode": ['balance-tcp'],
    "lacp_mode": ["active", "passive", "off"]
},
{
    "vlan_type": "vlan",
    "vswitch_type": ["dvs"],
    "bond_mode": ['active-backup', 'balance-slb'],
    "lacp_mode": ["off"]
},
{
    "vlan_type": "vlan",
    "vswitch_type": ["dvs"],
    "bond_mode": ['balance-tcp'],
    "lacp_mode": ["active", "passive", "off"]
}]

def find_data():
    ddd = dict(vlan_type = "vxlan", vswitch_type = "dvs", 
        bond_mode = "balance-tcp", lacp_mode = "passive")

    if ddd in available_combinations:
        print "Yes, it's in"
    else:
        print "No, not found"

if __name__ == "__main__":
    find_data()
