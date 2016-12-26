#!/bin/bash
aaa=$1

echo "start to ping..."
for i in `cat $aaa`
do
ping -c 1 $i
message=$?
if [ $message -ne 0 ]
then echo $i>>error.txt
else
echo $i>>right.txt
fi
done
