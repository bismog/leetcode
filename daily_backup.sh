
todayxxx=`date +%Y-%m-%d`
cd /home/cleancode_bak_daily/
rm -rf $todayxxx
mkdir $todayxxx
cd $todayxxx
#scp below need: current host "ssh-keygen" and "ssh-copy-id cml01" first
scp -r root@cml01:/home/cleancode/ ./
test $? -eq 0 && (find ./ | cpio -o > $todayxxx.cpio) || (cd ..; rm -rf $todayxxx)

