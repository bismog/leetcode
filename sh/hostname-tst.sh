#!/bin/bash

#if hostname | grep -q "cml01"; then
#    echo "result non-zero."
#else
#    echo "result zero"
#fi

hostname | grep -q "cml"
echo "result is $?"
oooggg=`hostname | grep -q cml`
echo "output is $oooggg."
if $oooggg; then
    echo "output non-blank."
else
    echo "output blank"
fi

