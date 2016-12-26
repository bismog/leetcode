#!/usr/bin/env bash
# move_local_dynamic_files_out.sh:
# Up to now, we have found follow files or directories are dynamically 
# generated in unittest installation and execution. After we modifying
# code, we should run this script before commit changing to svn server.
# And after committing, we can run move_local_dynamic_files_back.sh to recover
# the unittest scenarios.

# We assume current directory is PODManager/tools/, and we should run 
# this script in this directory.
cd ../
#check current directory, should be ./PODManager
cur_dir=`pwd`
cur_dir_name=`basename $cur_dir`
if [[ ! -d $cur_dir ]] || [[ $cur_dir_name != "PODManager" ]] 
then
    echo "please cd /path/to/PODManager/tools/ and run move_local_dynamic_files_out.sh"
fi

tmpdir=.xX.Xx.  #better than mktemp?
TMPFILE1=/tmp/$tmpdir/local.out
TMPFILE2=/tmp/$tmpdir/local.filter.out
if [[ -d /tmp/$tmpdir ]]
then
    rm -rf /tmp/$tmpdir
    mkdir -p /tmp/$tmpdir
fi

#temporarily mv ".svn" ".venv" ".testrepository"
if [[ -d podm/podm/.testrepository ]]
then
    echo "mv podm/podm/.testrepository /tmp/$tmpdir/"
    #mv podm/podm/.testrepository /tmp/$tmpdir/
fi

if [[ -d podm/podm/.venv ]]
then
    echo "mv podm/podm/.testrepository /tmp/$tmpdir/"
    #mv podm/podm/.venv /tmp/$tmpdir/
fi

#find .svn path and move out, maybe more than one .svn exist
#absolutely we have no need to work with .svn
#dotsvn_paths=`find ./ -type d -name ".svn"`
#for dotsvn_path in $dotsvn_paths
#do
#    if [[ -d $dotsvn_path ]]
#    then
#        #mkdir -p /tmp/$tmpdir/$dotsvn_path
#        #mv $dotsvn_path /tmp/$tmpdir/$dotsvn_path
#        echo "mkdir /tmp/$tmpdir/$dotsvn_path"
#        echo "mv $dotsvn_path /tmp/$tmpdir/$dotsvn_path"
#    fi
#done

#find .log / .err / .pyc file
find ./ | sed -e 's/^\.\///' -e '/\.svn/d' -e '/\/\..*/d' >$TMPFILE1 
#sed -n '/\/\..*/p' $TMPFILE1 > $TMPFILE2
sed -n '/\.log$/p'  $TMPFILE1 > $TMPFILE2
sed -n '/\.err$/p' $TMPFILE1 >> $TMPFILE2
sed -n '/\.pyc$/p' $TMPFILE1 >> $TMPFILE2
sed -n '/\.swp$/p' $TMPFILE1 >> $TMPFILE2
sort -u $TMPFILE2 -o $TMPFILE2

while read line
do
    filename=`basename $line`
    #mv $line  /tmp/$tmpdir/$filename
    echo "mv $line /tmp/$tmpdir/$filename"
done < $TMPFILE2

#move .svn back
#for dotsvn_path in $dotsvn_paths
#do
#    #mv /tmp/$tmpdir/$dotsvn_path $dotsvn_path
#    echo "mv /tmp/$tmpdir/$dotsvn_path $dotsvn_path"
#done

###############################################################################

#commit change to svn server
svn ci -m $descriptions ./

###############################################################################
#move .venv .testrepository and other such as .log .err .pyc back
mv /tmp/$tmpdir/.venv podm/podm/.venv
mv /tmp/$tmpdir/.testrepository podm/podm/.testrepository
while read line
do
    mv /tmp/$tmpdir/$filename  $line
done < $TMPFILE2

