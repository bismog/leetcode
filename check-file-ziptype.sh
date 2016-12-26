#!/bin/sh
filename=/home/chml/shell/tar-and-zip/control.tar.gz
ftype=`file $filename`
case "$ftype" in
"$filename: Zip archive"*)
    echo "this is zip file";;
"$filename: gzip compressed"*)
    echo "this is gzip tar file";;
"$filename: bzip2 compressed"*)
#    bunzip2 "$filename" ;;
    echo "this is bzip2 tar file";;
    
"$filename: POSIX tar archive"*)
    echo "this is simple tar file";;
*) echo "File $filename can not be uncompressed with smartzip";;
esac
