#!/usr/bin/env bash

#assume source packages all ready in current directory

#find only current directory, not in subdirectory
dependencies=/tmp/dependencies.list
if [ -f $dependencies ];then
    rm -rf $dependencies
	touch $dependencies
fi

all_rpms=`find ./ -maxdepth 1 -name "*.rpm" | gawk -F "/" '{print $2}'`
for rpm in $all_rpms
do
    rpm -qpR $rpm | gawk -F "(" '{print $1}' >> $dependencies
done

cat $dependencies | sort -u -o $dependencies
#echo '--------------------------------------------------------'
#cat $dependencies
#echo '--------------------------------------------------------'

depout=/tmp/depout.list
if [ -f $depout ];then
    rm -rf $depout
	touch $depout
fi
#find packages that provide file list in $dependencies
while read line
do
    outs=`repoquery --whatprovides $line` 
    if [[ -z $outs ]];then
        #echo "[ ]    $line:    no related package found" >> $depout
        printf "%s%-40s%s\n" "[ ]    " "$line:" "no related package found" >> $depout
    else
        #replace LF with ' '
        out_trimmed=`echo $outs | tr "\n" " "`
        #out_trimmed=$outs
        #echo "[x]    $line:    $out_trimmed" >> $depout
        printf "%s%-40s%s\n" "[x]    " "$line:" "$out_trimmed" >> $depout
    fi
done < $dependencies

#sort -u $depout -o $depout
#grep . $depout > $depout
sed -i '/^$/d' $depout
echo '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
cat $depout | sort -k1,1
echo '---------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
