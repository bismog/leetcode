#!/bin/bash

aaa="good"
bbb="bad"
#if $aaa = 'good'; then
#if [ $aaa = "good" ] and [ $bbb = "bad" ]; then
if [ $aaa = "good" ] && [ $bbb = "bad" ]; then
    echo "all right!"
else
    echo "not all right."
fi
# and $bbb = "bad"
