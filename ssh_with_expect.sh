#!/usr/bin/expect

set usr "root"
set host "cml02"
set psd "ztescs"
spawn ssh "$usr@$host"
expect "$usr@$host's password:"
send "$psd\r"
#interact
expect "# " 
#send "ps -elf \r"
#expect "# "
#send "ls /;ls /home\r"
#expect "# "

#copy and execute a shell script
send "scp root@cml03:/home/chml/echo_tmp.sh /home/chml\r"
expect "password"
send "ztescs\r"
expect "# "
send "sh /home/chml/echo_tmp.sh\r"

expect "# "
send "exit\r"
