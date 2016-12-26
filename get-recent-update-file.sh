#!/bin/sh

sourcefile=/home/chml/shell/resource-of-sort.txt

get_max_time_stamp()
{
#    local sourcefile=$1
    local max_time_stamp=0

    local sourcefile=/home/chml/shell/resource-of-sort.txt

    file_lists=`cat $sourcefile`
    echo "\$1 is $file_lists"

    for filestr in $file_lists; do
        local relative_name=${filestr##*/}
        local relative_name_no_ext=${relative_name%.*}
        local time_stamp=${relative_name_no_ext##*_}

        if [ $time_stamp -gt $max_time_stamp ];then
            max_time_stamp=$time_stamp
        fi
    done

    echo "max time stamp is $max_time_stamp"

    return $max_time_stamp
}

max_time_stamp=0
#for filestr in $file_lists; do
#    echo $filestr
#    relative_name=basename $filestr
#    relative_name=${filestr##*/}
#    echo $relative_name
#    relative_name_no_ext=${relative_name%.*}
#    time_stamp=${relative_name_no_ext##*_}
#    if [ $time_stamp -gt $max_time_stamp ];then
#        max_time_stamp=$time_stamp
#    fi
#done

max_time_stamp=get_max_time_stamp $sourcefile
echo $max_time_stamp

