str1="MATCH"
str2='match'

shopt -s nocasematch
case $str1 in
$str2) echo 'match';;
*) echo 'not match';;
esac

awk -v s1=$str1 -v s2=$str2 'BEGIN {
if(tolower(s1) == tolower(s2)) 
    print "match"
}'



