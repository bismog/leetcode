#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import sys
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker

def main(dump_file='/tmp/cluster_nodes.json'):
    engine = create_engine('mysql+mysqldb://daisy:daisy@127.0.0.1:13306/daisy?charset=utf8')
    Session = sessionmaker(bind=engine)
    session = Session()

    sql = text('select distinct hosts.name,assigned_networks.ip,hosts.root_user,hosts.root_pwd from networks,assigned_networks,host_interfaces,hosts where networks.network_type="MANAGEMENT" and networks.deleted=0 and assigned_networks.network_id=networks.id and host_interfaces.id=assigned_networks.interface_id and host_interfaces.host_id=hosts.id')
    target_nodes = session.execute(sql).fetchall()

    cnodes={"nodes":[dict(host=n[0], ip=n[1], usr=n[2], psd=n[3], ) for n in target_nodes]}
    with open(dump_file, 'w') as cn_file:
        json.dump(cnodes, cn_file)


if __name__ == "__main__":
    dump_file = sys.argv[1]
    main(dump_file)
