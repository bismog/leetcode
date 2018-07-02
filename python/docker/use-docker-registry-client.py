
from docker_registry_client import DockerRegistryClient
import docker

client = DockerRegistryClient("http://127.0.0.1:5000")
print client.repositories()
r = client.repository("busybox")
tags = r.tags()
print tags

docker_client = docker.from_env()
reg = docker_client.containers.get("registry")
print reg
docker_client.login(registry="http://127.0.0.1:5000", username="", password="")
docker_client.images.pull("127.0.0.1:5000/busybox")

