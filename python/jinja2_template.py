#!/usr/bin/env python

import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(os.path.join(PATH, 'templates')))
 
mac_addr = "01:23:45:67:89:01"
PXE_ROOT_DIR = "/data/tftpboot"
pxe_options = {
    'os_distribution': 'centos7',
    'path_to_vmlinuz': os.path.join(PXE_ROOT_DIR, 'node', mac_addr, 'vmlinuz'),
    'path_to_initrd': os.path.join(PXE_ROOT_DIR, 'node', mac_addr, 'initrd.img'),
    'path_to_kickstart_cfg': os.path.join(PXE_ROOT_DIR, 'node', mac_addr, 'ks.cfg'),
    'pxe_server_ip': '128.0.0.1',
    'protocol': 'nfs'
}

def build_pxe_config(ctxt, template):
    """Build the PXE boot configuration file.

    This method builds the PXE boot configuration file by rendering the
    template with the given parameters.

    :param pxe_options: A dict of values to set on the configuration file.
    :param template: The PXE configuration template.
    :param root_tag: Root tag used in the PXE config file.
    :param disk_ident_tag: Disk identifier tag used in the PXE config file.
    :returns: A formatted string with the file content.

    """
    tmpl_path, tmpl_file = os.path.split(template)
    env = Environment(loader=FileSystemLoader(tmpl_path))
    template = env.get_template(tmpl_file)
    return template.render(ctxt)

def get_pxe_mac_path(mac, delimiter=None):
    """Convert a MAC address into a PXE config file name.

    :param mac: A MAC address string in the format xx:xx:xx:xx:xx:xx.
    :param delimiter: The MAC address delimiter. Defaults to dash ('-').
    :returns: the path to the config file.

    """
    if delimiter is None:
        delimiter = '-'

    mac_file_name = mac.replace(':', delimiter).lower()
    mac_file_name = '01-' + mac_file_name

    return os.path.join(PXE_ROOT_DIR, 'pxelinux.cfg', mac_file_name)
 
def get_teml_path():
    """
    """
    return os.path.join(PXE_ROOT_DIR, 'template', '01-xx-xx-xx-xx-xx-xx.template')


#def render_template(template_filename, context):
#    return env.get_template(template_filename).render(context)
 
 
def create_pxe_config_file(pxe_options):
    # fname = "output.html"
    cname = get_pxe_mac_path(mac_addr)
    tname = get_teml_path()
    context = {
        'pxe_opts': pxe_options
    }

    with open(cname, 'w') as f:
        config = build_pxe_config(context, tname)
        f.write(config)
 
 
########################################
 
if __name__ == "__main__":
    create_pxe_config_file(pxe_options)
