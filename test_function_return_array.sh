#!/bin/sh

arraydblr()
{
    local origarray
    local newarray
    local elements
    local i
    origarray=(`echo "$@"`)
    newarray=(`echo "$@"`)
    #echo "get $[ $#-1 ] parameter"
    elements=$[ $#-1 ]
    #echo "elements:$elements"

    for ((i=0;i<=$elements;i++))
    {
        newarray[$i]=$[ ${origarray[$i]}*2 ]
    }
    echo ${newarray[*]}
}

myarray=(1 2 3 4 5)
echo "the original array is:${myarray[*]}"
#argl=`echo ${myarray[*]}`
#result=(`arraydblr $argl`)
result=(`arraydblr ${myarray[*]}`)
echo "the new array is:${result[*]}"
