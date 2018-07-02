import tarfile


## https://pymotw.com/2/tarfile/

out_file = tarfile.open("/run/tmp/tarfile_add.tar", "w")
out_file.add("/run/tmp/aaa")
out_file.add("/run/tmp/bbb")
out_file.close()

open_file = tarfile.open("/run/tmp/tarfile_add.tar", "r")
for member in open_file.getmembers():
    print member.name

print open_file.getnames()
