#!/usr/bin/env python

import pexpect

if __name__ == "__main__":
    usr = "companyxxx"
    psd = "companyxxx"
    host = "128.128.0.166"
    en_psd = "zxr10"

    pe = pexpect.spawn("telnet %s" % host)
    pe.logfile = file("/tmp/pe.log", "w")  #function file can be substituded with open
    pe.expect("Username")
    pe.sendline("%s" % usr)
    pe.expect("Password")
    pe.sendline("%s" % psd)
    pe.expect("ZXR10>")
    pe.sendline("enable")
    pe.expect("Password")
    pe.sendline("%s" % en_psd)
    pe.expect("ZXR10#")
    pe.sendline("show version")
    pe.expect("More")
    pe.sendline(" ")
    pe.expect("#")
    pe.sendline("exit")
