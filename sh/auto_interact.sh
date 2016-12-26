#!/usr/bin/env expect


set usr "zte"
set psd "zte"
set en_psd "zxr10"
set host "128.128.0.166"

spawn telnet $host
expect "Username"
send "$usr\r"
expect "Password"
send "$psd\r"
expect "ZXR10>"
send "enable\r"
expect "Password"
send "$en_psd\r"
expect "ZXR10#"
send "show version\r"
expect "ZXR10#"
send "exit\r"

