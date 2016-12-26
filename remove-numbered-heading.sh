#!/usr/bin/env bash

#srcfile=./nnh.md
srcfile=$1

sed -i -e 's/^\(#\+\).* /\1 /g' $srcfile
