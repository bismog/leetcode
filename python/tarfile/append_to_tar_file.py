import tarfile

out = tarfile.open("/run/tmp/tar_file_b.tar", "w")
out.add("/run/tmp/aaa")
out.close()

out = tarfile.open("/run/tmp/tar_file_b.tar", "a")
out.add("/run/tmp/bbb")
out.close()

out = tarfile.open("/run/tmp/tar_file_b.tar", "r")
print out.getnames()
