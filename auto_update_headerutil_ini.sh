#!/usr/bin/env bash


#create temp sub-directory in current and do all things in it
TMP_DIR=$(mktemp -d)
cd $TMP_DIR
BOARDID_XLS_FILE=boardid.xls
BOARDID_TEXT_FILE=${BOARDID_XLS_FILE%.*}.text
TRIMMED_FILE=${BOARDID_XLS_FILE%.*}.trim
AUTO_UPDATE_LOG_PATH=/tmp/headerutil_log
AUTO_UPDATE_LOG=auto_update_headerutil_$(date +%Y-%m-%d).log
HEADERUTIL_FILE=HeaderUtil/HeaderUtil.ini
touch $BOARDID_TEXT_FILE
touch $TRIMMED_FILE
mkdir -p ${AUTO_UPDATE_LOG_PATH}
cd ${AUTO_UPDATE_LOG_PATH}
touch $AUTO_UPDATE_LOG
AUTO_UPDATE_LOG_WHOLE_PATH=${AUTO_UPDATE_LOG_PATH}/${AUTO_UPDATE_LOG}
cd $TMP_DIR

#get boardid.xls and check out HeaderUtil from svn
svn cat http://10.43.25.227/svn/3gplatdoc/trunk/3GPLATDOC/3GPLAT/32\ 平台部门管理/设计开发一部/03\ 研发流程/单板ID分配表.xls > $BOARDID_XLS_FILE
HEADERUTIL_URL="http://10.43.25.237/svn/OutCodeTool/trunk/3gplatout/outcode/%E5%A4%96%E6%9D%A5%E4%BB%A3%E7%A0%81%E5%92%8C%E5%B7%A5%E5%85%B7%E4%BB%A3%E7%A0%81/04-%E8%87%AA%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7/V4%E6%89%8B%E5%8A%A8%E5%8A%A0%E5%A4%B4%E5%B7%A5%E5%85%B7/HeaderUtil"
svn co $HEADERUTIL_URL

#convert from xls to csv, each sheet a output file
#for i in {1..$SHEET_COUNT}; do
#only sheet3 and sheet4 is what we need
for((i=3; i<=4; i++)); do
    CSV_FILE_NAME=sheet$i.csv
    xls2csv -f -x $BOARDID_XLS_FILE -n $i -b WINDOWS-1252 -c $CSV_FILE_NAME -a UTF-8 #2>&1 >>$AUTO_UPDATE_LOG_WHOLE_PATH #1251 also work
done

#read data from (*.csv)s, merge all the datas into one text file (skip sheet1.csv for this is a log sheet)
#only sheet3 and sheet4 is what we need
for((i=3; i<=4; i++)); do
    CSV_FILE_NAME=sheet$i.csv
    while read line; do
        echo $line >> $BOARDID_TEXT_FILE 
    done < $CSV_FILE_NAME
done

# trimming:
# x. delete line with ",,,,,,,"
# x. replace multi ',' with single ','
# x. use ',' as seperator, if $4 is all digit string, then print $2 and $4 (also known as boardname and decimal boardid value)
# x. delete '/' or '_' in boardname string
sed '/,,,,,,,/d' $BOARDID_TEXT_FILE | tr -s ',' ',' | gawk -F "," '{if($4 ~ /^[0-9]+$/) print $2":"$4;}' | tr -d "[/_]" > $TRIMMED_FILE

#for each board, search between 1~$auto_search_end_spot, if not found, insert "_BT_3G_$board_name = $boardid_value" in $auto_insert_spot
while read line; do
    board_name=${line%%:*}
    boardid_value=${line##*:}
    match_line=`sed -n '/auto_insert_spot/,/auto_search_end_spot/p' $HEADERUTIL_FILE | grep -n "_3G_$board_name " | gawk -F ":" '{print $1}'`
    #if there are more than one record for one board in HeaderUtil.ini, something may go wrong
    if [[ -n $match_line ]];then 
#set -xv
        if [[ ${match_line} -gt 0 ]]; then
#set +xv
            printf "%-10s%s\n" $board_name ":    [ already exist in line $match_line ]" >> $AUTO_UPDATE_LOG_WHOLE_PATH
        else
            printf "%-10s%s\n" $board_name ":    [ ERROR:sth may be wrong with this board, pls check $HEADERUTIL_FILE or ask for help ]" >> $AUTO_UPDATE_LOG_WHOLE_PATH
        fi
    else
        format_new_line=`printf "%-20s%s" "_BT_3G_$board_name" "=       $boardid_value"`
        sed -i '/auto_insert_spot/a\'"$format_new_line"'' $HEADERUTIL_FILE
        printf "%-10s%s\n" $board_name ":    [ inserting...  done! ]"  >> $AUTO_UPDATE_LOG_WHOLE_PATH
    fi
done < $TRIMMED_FILE

#if there is update for HeaderUtil.ini, svn commit it to server
if grep -q "inserting" $AUTO_UPDATE_LOG_WHOLE_PATH; then
    echo "svn ci HeaderUtil/HeaderUtil.ini ..." >> $AUTO_UPDATE_LOG_WHOLE_PATH
    svn ci -m "cml:updadte" $HEADERUTIL_FILE
else
    echo "no update, no need to commit." >> $AUTO_UPDATE_LOG_WHOLE_PATH
fi

#remove files except *.text and *.log
rm -rf $TMP_DIR/HeaderUtil
rm -rf $TMP_DIR/sheet3.csv $TMP_DIR/sheet4.csv
rm -rf $TMP_DIR/$BOARDID_XLS_FILE
rm -rf $TMP_DIR/$TRIMMED_FILE

echo "auto check and update accomplished, you can check log file $TMP_DIR/$AUTO_UPDATE_LOG_WHOLE_PATH for more information."












