#!/bin/sh

exec 3> testfile
echo "this is a test line of data" >&3
exec 3>&-

echo "this won't work" >&3
