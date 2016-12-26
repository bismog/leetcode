#!/usr/bin/env sh

#des=`cat description.log`
#echo -e $des
#cat description.log | while read line

while read line
do
#    echo $line
    if [ -z $line ]
    then
        des=$des"\n"
    else
        des=$des$line
    fi
done < description.log
echo -e $des
