#!/usr/bin/env bash

endpoint_proto=$1

service_id=$(keystone service-list | awk '/ identity / {print $2}')
endpoint_ids=$(keystone endpoint-list | awk -v pattern="$service_id" '$0 ~ pattern {print $2}')
for epid in $endpoint_ids; do
    keystone endpoint-delete $epid >/dev/null 2>&1
done
keystone endpoint-create \
  --service-id=$service_id \
  --publicurl=${endpoint_proto}://10.43.211.64:5000/v2.0 \
  --internalurl=${endpoint_proto}://10.43.211.64:5000/v2.0 \
  --adminurl=${endpoint_proto}://10.43.211.64:35357/v2.0 >/dev/null 2>&1

service_id=$(keystone service-list | awk '/ podm_v1 / {print $2}')
endpoint_ids=$(keystone endpoint-list | awk -v pattern="$service_id" '$0 ~ pattern {print $2}')
for epid in $endpoint_ids; do
    keystone endpoint-delete $epid >/dev/null 2>&1
done
keystone endpoint-create \
  --service-id=$service_id \
  --publicurl=${endpoint_proto}://10.43.211.64:8777/rest/v1 \
  --internalurl=${endpoint_proto}://10.43.211.64:8777/rest/v1 \
  --adminurl=${endpoint_proto}://10.43.211.64:8777/rest/v1 >/dev/null 2>&1

service_id=$(keystone service-list | awk '/ podmv1_extra / {print $2}')
endpoint_ids=$(keystone endpoint-list | awk -v pattern="$service_id" '$0 ~ pattern {print $2}')
for epid in $endpoint_ids; do
    keystone endpoint-delete $epid >/dev/null 2>&1
done
keystone endpoint-create \
  --service-id=$service_id \
  --publicurl=${endpoint_proto}://10.43.211.64:8777/rest/v1/%\(tenant_id\)s \
  --internalurl=${endpoint_proto}://10.43.211.64:8777/rest/v1/%\(tenant_id\)s \
  --adminurl=${endpoint_proto}://10.43.211.64:8777/rest/v1/%\(tenant_id\)s >/dev/null 2>&1
