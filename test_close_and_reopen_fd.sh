#!/bin/sh

exec 3> testfile
echo "this is a test line of data" >&3
##exec 3>&-

##cat testfile

exec 3> testfile #if redirect, it means file discriptor recreate
echo "this'll be bad" >&3
##exec 2> testfile
##echo "this'll be bad" >&2

