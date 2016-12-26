#!/bin/sh

for (( a=1; a < 5; a++ ))
do
    echo "iteration $a"
    for (( b=1; b<3; b++  ))
    do
        if [ $a -gt 2 ] && [ $a -lt 4 ]
        then 
            #continue 2
            continue
        fi
        var3=$[ $a*$b ]
        echo "result of $a*$b is $var3"
    done
done
