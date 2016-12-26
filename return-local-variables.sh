#!/bin/sh

funx()
{
   local vvx=abcd
   vvy=436

   return $vvy
}

xxx=`funx`
echo "output is $xxx"
echo "return code is $?"
#ret_of_funx=`echo $?`
#echo $ret_of_funcx
