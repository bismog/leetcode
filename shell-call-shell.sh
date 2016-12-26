#!/bin/sh
#CURDIR="`pwd`"/"`dirname $0`"
CURDIR="`pwd`"

echo $CURDIR
#.$CURDIR/shell-to-be-call.sh
sh $CURDIR/shell-to-be-call.sh

a="TEST"
export a
#set -a
./b.sh

