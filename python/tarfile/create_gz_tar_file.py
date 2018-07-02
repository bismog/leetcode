import tarfile

out = tarfile.open("/run/tmp/tar_out_c.tar.gz", "w:gz")
out.add("/run/tmp/aaa")
out.add("/run/tmp/bbb")
out.close()

out = tarfile.open("/run/tmp/tar_out_c.tar.gz", "r:*")
print out.getnames()
