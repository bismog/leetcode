#!/usr/bin/env python

pxe_tool_url = "http://"
daisy_url = "http://artifacts.zte.com.cn/artifactory/api/storage/zxtecs-release-local/tecs2.0/daisy/Bugfix_P8B2/"

from artifactory import ArtifactoryPath

# path = ArtifactoryPath(pxe_tool_url)
path = ArtifactoryPath(daisy_url)
for p in path:
    print p


