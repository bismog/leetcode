#!/usr/bin/env bash

#srcfile=./nnh.md
srcfile=$1

replace()
{
    local level=$1
    local sharps=$(printf '%0.s#' $(seq 1 $level))
    local base_numbered_string=''
    [[ $level != '1' ]] && base_numbered_string=$(printf '%0.s1.' $(seq 1 $(expr $level - 1)))
    local last_number=1
    while true; do
        #echo "sharps is /$sharps/"
        local out=$(sed -n -e '/^'"${sharps}"' /p' ${srcfile})
        [[ $out ]] || return
        last_number=$(expr $last_number + 1)
        sed -i -e '0,/^'"${sharps}"' /s/^'"${sharps}"' /'"${sharps}"''"${base_numbered_string}"''"${last_number}"' /' $srcfile
   done 
}


slist=$(seq 1 6)
for i in $slist;do
    replace $i
done
