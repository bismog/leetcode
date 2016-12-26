#!/bin/bash

exclude_file_list="d.s w.q yy6"

function smatch() {
    for efl in $exclude_file_list
    do
        echo "$1" | grep -q "$efl"
        if [ $? -eq 0 ]
        then
            echo "include"
            return
        else
            continue
        fi
    done
    echo "uninclude"
}

function ergodic(){
  for file in `ls $1`
  do
    if [ -d $1"/"$file ]
    then
      ergodic $1"/"$file
    else
      local abs_dir=$1"/"$file
      return=`smatch $abs_dir`
      if [[ "include" = $return ]]
      then
          echo "$abs_dir        -- discard."
          continue
      else
          echo "$1/$file" 
      fi
    fi
  done
}
INIT_PATH="/home/chml/shell/candel"
ergodic $INIT_PATH
