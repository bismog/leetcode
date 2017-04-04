#!/usr/bin/env bash

set -eux

# For example, 1335
VERSION=$1

# Remove legacy daisy rpm
# rpm -e daisy

# Download and install daisy rpm
# cd /tmp
# curl -O -u daisy:isyda http://artifacts.zte.com.cn/artifactory/zxtecs-release-local/tecs2.0/daisy/upstreamfirst_docker/daisy-2016.2.11-upstreamfirst.1.${VERSION}.el7.x86_64.rpm
# rpm -ivh /tmp/daisy-2016.2.11-upstreamfirst.1.1335.el7.x86_64.rpm

# Run daisy container
# sed -i '/dashboard\ ip\ input/d' /usr/bin/daisy_docker_init.sh
# daisy_docker_init.sh eth0 192.167.1.137 10.43.174.101

# Prepare
# docker cp /etc/yum.repos.d/centos7.repo daisy:/etc/yum.repos.d/
# docker cp /home/tools/schemaspy/schemaspy_5.0.0.jar daisy:/
# sleep 20
docker exec -it daisy '/usr/bin/yum install --disablerepo=* --enablerepo=centos7 -y java-1.8.0-openjdk mysql-connector-java graphviz'
sed -i '/port/d' /etc/my.cnf

# Generate database schema
docker exec -it daisy 'mkdir -p /home/daisydb/'
docker exec -it daisy '/usr/bin/java -jar schemaspy_5.0.0.jar -t mysql -host localhost -db daisy -u daisy -p daisy -s public -dp /usr/share/java/mysql-connector-java.jar -o /home/daisydb/'

# Copy and publish
docker cp daisy:/home/daisydb /home/refer/daisy/database/

# We can check database schema via http://10.43.174.101/refer/daisy/database/daisydb/
