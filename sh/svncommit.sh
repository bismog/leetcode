#!/usr/bin/env bash

# Up to now, we have found follow files or directories are dynamically 
# generated in unittest installation and execution. After we modifying
# code, we can run this script to commit changing to svn server.

# usage
if [ $# = 1 ]; then
    descriptions=$1
else
    echo "usage: ./svncommit.sh \"description for this commit\""
    exit
fi


# We assume current directory is PODManager/tools/, and we should run 
# this script in this directory.
cd ../
#check current directory, should be ./PODManager
cur_dir=`pwd`
cur_dir_name=`basename $cur_dir`
if [[ ! -d $cur_dir ]] || [[ $cur_dir_name != "PODManager" ]] 
then
    echo "please cd /path/to/<PODManager/tools>/ and run this script."
    exit
fi

#tmpdir=.xXx.  #better than mktemp?
tmpdir=`mktemp -d -p /tmp/`
TMPFILE1=$tmpdir/local.out
TMPFILE2=$tmpdir/local.filter.out
if [[ -d $tmpdir ]]
then
    rm -rf $tmpdir
    mkdir -p $tmpdir
else
    mkdir -p $tmpdir
fi

#temporarily mv ".svn" ".venv" ".testrepository"
if [[ -d $cur_dir/podm/podm/.testrepository ]]
then
    mv podm/podm/.testrepository $tmpdir/
fi

if [[ -d $cur_dir/podm/podm/.venv ]]
then
    mv podm/podm/.venv $tmpdir/
fi

#find .log / .err / .pyc / .swp file
find ./ | sed -e 's/^\.\///' -e '/\.svn/d' -e '/\/\..*/d' >$TMPFILE1 
sed -n '/\.log$/p'  $TMPFILE1 > $TMPFILE2
sed -n '/\.err$/p' $TMPFILE1 >> $TMPFILE2
sed -n '/\.pyc$/p' $TMPFILE1 >> $TMPFILE2
sed -n '/\.swp$/p' $TMPFILE1 >> $TMPFILE2
sort -u $TMPFILE2 -o $TMPFILE2

#while read line
#do
#    filename=`basename $line`
#    mv $line  /tmp/$tmpdir/$filename
#    echo "mv $line /tmp/$tmpdir/$filename"
#done < $TMPFILE2
while read line
do
    relative_path=`dirname $line`
    base_file_name=`basename $line`
    mkdir -p $tmpdir/$relative_path
    mv $line $tmpdir/$relative_path/$base_file_name
done < $TMPFILE2

###############################################################################

#commit change to svn server
svn ci -m "$descriptions" *
echo "svn ci -m \"$descriptions\" *"

###############################################################################
#move .venv .testrepository and other such as .log .err .pyc back
if [[ -d $cur_dir/podm/podm ]]
then
    mv $tmpdir/.venv podm/podm/.venv
    mv $tmpdir/.testrepository podm/podm/.testrepository
fi

while read line
do
    relative_path=`dirname $line`
    base_file_name=`basename $line`
    if [[ ! -d $cur_dir/$relative_path ]]
    then
        mkdir -p $cur_dir/$relative_path
    fi
    mv $tmpdir/$relative_path/$base_file_name $line
done < $TMPFILE2

#remove temp directory
rm -rf $tmpdir
