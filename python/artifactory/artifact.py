#!/usr/bin/env python

pxe_tool_url = "http://"
projectxxx_url = "http://artifacts.companyxxx.com.cn/artifactory/api/storage/zxproject0xxx-release-local/project0xxx2.0/projectxxx/Bugfix_P8B2/"

from artifactory import ArtifactoryPath

# path = ArtifactoryPath(pxe_tool_url)
path = ArtifactoryPath(projectxxx_url)
for p in path:
    print p


