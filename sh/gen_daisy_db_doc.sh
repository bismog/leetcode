#!/usr/bin/env bash

set -eux

# For example, 1335
VERSION=$1

# Remove legacy projectxxx rpm
# rpm -e projectxxx

# Download and install projectxxx rpm
# cd /tmp
# curl -O -u projectxxx:isyda http://artifacts.companyxxx.com.cn/artifactory/zxproject0xxx-release-local/project0xxx2.0/projectxxx/upstreamfirst_docker/projectxxx-2016.2.11-upstreamfirst.1.${VERSION}.el7.x86_64.rpm
# rpm -ivh /tmp/projectxxx-2016.2.11-upstreamfirst.1.1335.el7.x86_64.rpm

# Run projectxxx container
# sed -i '/dashboard\ ip\ input/d' /usr/bin/projectxxx_docker_init.sh
# projectxxx_docker_init.sh eth0 192.167.1.137 10.43.174.101

# Prepare
# docker cp /etc/yum.repos.d/centos7.repo projectxxx:/etc/yum.repos.d/
# docker cp /home/tools/schemaspy/schemaspy_5.0.0.jar projectxxx:/
# sleep 20
docker exec -it projectxxx '/usr/bin/yum install --disablerepo=* --enablerepo=centos7 -y java-1.8.0-openjdk mysql-connector-java graphviz'
sed -i '/port/d' /etc/my.cnf

# Generate database schema
docker exec -it projectxxx 'mkdir -p /home/projectxxxdb/'
docker exec -it projectxxx '/usr/bin/java -jar schemaspy_5.0.0.jar -t mysql -host localhost -db projectxxx -u projectxxx -p projectxxx -s public -dp /usr/share/java/mysql-connector-java.jar -o /home/projectxxxdb/'

# Copy and publish
docker cp projectxxx:/home/projectxxxdb /home/refer/projectxxx/database/

# We can check database schema via http://10.43.174.101/refer/projectxxx/database/projectxxxdb/
