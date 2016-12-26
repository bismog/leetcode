#!/bin/sh

factorial()
{
    if [ $1 -eq 1 ]
    then
        echo 1
    else
        local tmp=$[ $1-1 ]
        local result=`factorial $tmp`
        echo $[ $result*$1 ]
    fi
}

read -p "please enter a value:" value
result=`factorial $value`
echo "the factorial result of $value is: $result"
