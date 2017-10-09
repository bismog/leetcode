#!/usr/bin/env python

from oslo.config import cfg

dhcp_opts = [
    cfg.StrOpt("dhcp_config_file",
               default = "/etc/dhcp/dhcpd.conf",
               help = "dhcp server configuration file"),
    cfg.ListOpt("dhcp_option_params",
               default = ['domain-name-servers', 'routers' , 'broadcast-address'],
               help = "dhcp parameters with option prefix"),
    cfg.StrOpt("dhcp_next_server",
               default = "129.128.0.1",
               help = "dhcp server ip address"),
    cfg.StrOpt("dhcp_bootstrap_filename",
               default = '"pxelinux.0"',
               help = "bootstrap file name"),
    cfg.IntOpt("dhcp_default_lease_time",
               default = 1800,
               help = "default lease time"),
    cfg.IntOpt("dhcp_max_lease_time",
               default = 7200,
               help = "maximum lease time"),
    cfg.StrOpt("dhcp_ping_check",
               default = "true",
               help = "ping to check whether ip has been used before assigning"),
    cfg.StrOpt("dhcp_domain_name_servers",
               default = "129.128.0.1",
               help = "domain name server ip addresses"),
    cfg.StrOpt("dhcp_subnet",
               default = "129.128.0.0",
               help = "subnet"),
    cfg.StrOpt("dhcp_netmask",
               default = "255.255.0.0",
               help = "netmask"),
    cfg.StrOpt("dhcp_range_min",
               default = "129.128.0.100",
               help = "lower limit of assignable ip address range"),
    cfg.StrOpt("dhcp_range_max",
               default = "129.128.0.200",
               help = "upper limit of assignable ip address range"),
    cfg.StrOpt("dhcp_routers",
               default = "129.128.0.1",
               help = "routers ip addresses"),
    cfg.StrOpt("dhcp_broadcast_address",
               default = "129.128.255.255",
               help = "broadcast ip address"),
]

CONF = cfg.CONF
CONF.register_opts(dhcp_opts)

content_model = \
'''authoritative;
ddns-update-style interim;
allow booting;
allow bootp;
next-server %(dhcp_next_server)s;
filename %(dhcp_bootstrap_filename)s;

default-lease-time %(dhcp_default_lease_time)d;
max-lease-time %(dhcp_max_lease_time)d;
ping-check %(dhcp_ping_check)s;
option domain-name-servers %(dhcp_domain_name_servers)s;

subnet %(dhcp_subnet)s netmask %(dhcp_netmask)s
{
        range %(dhcp_range_min)s  %(dhcp_range_max)s;
        option routers %(dhcp_routers)s;
        option broadcast-address %(dhcp_broadcast_address)s;
}
''' % CONF
print content_model
#ppp = "__%(dhcp_config_file)s_and__%(dhcp_next_server)s__and__%(dhcp_bootstrap_filename)s__" % CONF
#print ppp
