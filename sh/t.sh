#!/bin/sh

get_image() {
ftphead=ftp://
httphead=http://
#netpath=10.43.110.150/
tmpfilename=hnimg_tmp
filename=$1
proto=$2
netpath=$3
user=$4
pswd=$5

if [ "$proto" == "ftp" -o "$proto" == "FTP" ];then
#if [ "$proto" == "ftp" ];then
    head=$ftphead;
else
    head=$httphead;
fi

#echo "wget -O /ver/$tmpfilename -q $head$user:$pswd@$netpath/$filename"
#echo "wget start..."
#wget auto quit if cann't download in 30 seconds
wget -O /ver/$tmpfilename -T 30 -q  $head$user:$pswd@$netpath/$filename --spider 2>&1 >wget1err.log
if [ $? ];then
    echo OK!
else
    echo God Damn!
fi
#cmdstr=wget -O /ver/ -q >downloadinfo.txt 2>/tmp/downloaderr.txt
#echo "end of wget."

}


get_config() {
ftphead=ftp://
httphead=http://
#netpath=10.43.110.150/
tmpfilename=sysfirm_tmp
filename=$1
proto=$2
netpath=$3
user=$4
pswd=$5

if [ "$proto" == "ftp" -o "$proto" == "FTP" ];then
    head=$ftphead
else
    head=$httphead
fi

#echo "wget -O /ver/tmpfilename -q $head$user:$pswd@$netpath/$filename"
#echo "wget start..."
#wget -O /ver/$tmpfilename -T 10  $head$user:$pswd@$netpath/$filename 2>&1 | tee /tmp/wget.log
wget -O /ver/$tmpfilename -T 10  $head$user:$pswd@$netpath/$filename >/tmp/wget2.log 2>/tmp/wget2err.log
#cmdstr=wget -O /ver/ -q :@>downloadinfo1.txt 2>/tmp/downloaderr1.txt
#echo "end of wget."

}

bak_file(){
filename=$1
bakname=$filename.bak
mv $filename $bakname

}


endofsth(){

#remove bakfile
#rm -rf /ver/*.bak

#rename tmpfile
mv /ver/hnimg_tmp /ver/hnimage
mv /ver/sysfirm_tmp /ver/bootver.ini

}


#rename image and config file, from *** to ***.bak
echo -e "\cbak file..."
bak_file "/ver/hnimage"
bak_file "/ver/bootver.ini"
echo "bak file... done."

#download image and config file
echo -e "\cstart download config..."
get_config "Packages.gz" "ftp"  "10.43.110.150" "3gplat" "3gplat"
echo "start download config... done."

echo -e "\cstart download Img..."
get_image "hello_1.0-1_all.ipk" "ftp" "10.43.110.150" "3gplat" "3gplat"
echo "start download Img... done."

#rename tmpfile
echo "rename tmpfile..."
endofsth
echo "all done."
