#!/usr/bin/env bash

XLS_FILE_NAME=boardid_20150713.xls
#SHEET_COUNT=7

#create temp sub-directory in current and do all things in it
TMP_DIR=`mktemp -d -p ./`
cd $TMP_DIR
TEXT_FILE_NAME=${XLS_FILE_NAME%.*}.text
TRIMMED_FILE=${XLS_FILE_NAME%.*}.trim
AUTO_UPDATE_LOG=auto_update.log
HEADERUTIL_FILE=HeaderUtil/HeaderUtil.ini
touch $TEXT_FILE_NAME
touch $TRIMMED_FILE
touch $AUTO_UPDATE_LOG

#get boardid.xls and check out HeaderUtil from svn
cp ../boardid_20150713.xls ./   #temporarily copy from parent directory
HEADERUTIL_URL="http://10.43.25.237/svn/OutCodeTool/trunk/3gplatout/outcode/%E5%A4%96%E6%9D%A5%E4%BB%A3%E7%A0%81%E5%92%8C%E5%B7%A5%E5%85%B7%E4%BB%A3%E7%A0%81/04-%E8%87%AA%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7/V4%E6%89%8B%E5%8A%A8%E5%8A%A0%E5%A4%B4%E5%B7%A5%E5%85%B7/HeaderUtil"
svn co $HEADERUTIL_URL

#convert from xls to csv, each sheet a output file
#for i in {1..$SHEET_COUNT}; do
#only sheet3 and sheet4 is what we need
for((i=3; i<=4; i++)); do
    CSV_FILE_NAME=sheet$i.csv
    xls2csv -f -x $XLS_FILE_NAME -n $i -b WINDOWS-1252 -c $CSV_FILE_NAME -a UTF-8 #2>&1 >>$AUTO_UPDATE_LOG  #1251 also work
done

#read data from (*.csv)s, merge all the datas into one text file (skip sheet1.csv for this is a log sheet)
#only sheet3 and sheet4 is what we need
for((i=3; i<=4; i++)); do
    CSV_FILE_NAME=sheet$i.csv
    while read line; do
        echo $line >> $TEXT_FILE_NAME 
    done < $CSV_FILE_NAME
done

# trimming:
# x. delete line with ",,,,,,,"
# x. replace multi ',' with single ','
# x. use ',' as seperator, if $4 is all digit string, then print $2 and $4 (also known as boardname and decimal boardid value)
# x. delete '/' or '_' in boardname string
sed '/,,,,,,,/d' $TEXT_FILE_NAME | tr -s ',' ',' | gawk -F "," '{if($4 ~ /^[0-9]+$/) print $2":"$4;}' | tr -d "[/_]" > $TRIMMED_FILE


##get auto_insert_spot & auto_search_end_spot in HeaderUtil.ini
#auto_insert_spot_0=`grep -n "auto_insert_spot" $HEADERUTIL_FILE | gawk -F ":" '{print $1}'`
#auto_insert_spot=$[$auto_insert_spot_0+1]
#auto_search_end_spot=`grep -n "auto_search_end_spot" $HEADERUTIL_FILE | gawk -F ":" '{print $1}'`

#for each board, search between 1~$auto_search_end_spot, if not found, insert "_BT_3G_$board_name = $boardid_value" in $auto_insert_spot
while read line; do
    board_name=${line%%:*}
    boardid_value=${line##*:}
    #echo $board_name
    #how to match $board_name here?????????????????
    #match_line=`awk 'BEGIN {IGNORECASE=1} NR>=$auto_insert_spot_0 && NR<=$auto_search_end_spot &&(/$board_name/){print NR}' $HEADERUTIL_FILE`
    #echo $match_line
    #if [[ $match_line -gt $auto_insert_spot_0 ]] && [[ $match_line -lt $auto_search_end_spot_0 ]]; then
    #    echo "$board_name [already exist.]"
    #    continue;  #this board already exist
    #else
    #    #sed '/auto_insert_spot/a\_3G_BT_$board_name = $boardid_value' $HEADERUTIL_FILE
    #    echo "insert $board_name [done]"
    #fi

    #grep -n auto_insert_spot $HEADERUTIL_FILE
    #grep -n auto_search_end_spot $HEADERUTIL_FILE
    match_line=`sed -n '/auto_insert_spot/,/auto_search_end_spot/p' $HEADERUTIL_FILE | grep -n "_3G_$board_name " | gawk -F ":" '{print $1}'`
    #echo $board_name $match_line
    #if there are more than one record for one board in HeaderUtil.ini, something may go wrong
    if [[ -n $match_line ]];then 
#set -xv
        if [[ ${match_line} -gt 0 ]]; then
#set +xv
            printf "%-10s%s\n" $board_name ":    [ already exist in line $match_line ]" >> $AUTO_UPDATE_LOG
        else
            printf "%-10s%s\n" $board_name ":    [ ERROR:sth may be wrong with this board, pls check $HEADERUTIL_FILE or ask for help ]" >> $AUTO_UPDATE_LOG
        fi
    else
        #printf "%-20s%s\n" "_3G_BT_$board_name" "=       $boardid_value"
        format_new_line=`printf "%-20s%s" "_BT_3G_$board_name" "=       $boardid_value"`
        #echo "$format_new_line"
        sed -i '/auto_insert_spot/a\'"$format_new_line"'' $HEADERUTIL_FILE
        printf "%-10s%s\n" $board_name ":    [ inserting...  done! ]"  >> $AUTO_UPDATE_LOG
    fi
done < $TRIMMED_FILE

echo "pls check $TMP_DIR/$AUTO_UPDATE_LOG for log"

#svn commit to server
echo "svn ci HeaderUtil/HeaderUtil.ini ..."
svn ci -m "cml:updadte" $HEADERUTIL_FILE
echo "done."












