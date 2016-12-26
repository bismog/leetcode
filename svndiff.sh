#!/usr/bin/env bash

if [ $# = 3 ]; then  # format 1
    RECORD_A=$1
    RECORD_B=$2
    FILE=$3
    BASE_FILE=`basename $FILE`
elif [ $# = 2 ]; then
    RECORD_A=$[$1-1]
    RECORD_B=$1
    FILE=$2
    BASE_FILE=`basename $FILE`
else
    echo "usage: svndiff r_a r_b file  #compare r_a with r_b"       # format 1
    echo "    or svndiff r_b file      #compare r_b-1 with r_b"     # format 2
    exit
fi

TEMP_A=/tmp/$RECORD_A.tmp.$BASE_FILE
TEMP_B=/tmp/$RECORD_B.tmp.$BASE_FILE

svn cat -r $RECORD_A $FILE > $TEMP_A  
svn cat -r $RECORD_B $FILE > $TEMP_B  

vimdiff $TEMP_A $TEMP_B
rm -rf $TEMP_A $TEMP_B
