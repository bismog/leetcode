
import pexpect

if __name__ == "__main__":
    usr = "root"
    psd = "companyxxxscs"
    host = "10.43.177.146"

    pe = pexpect.spawn("ssh %s" % host)
    pe.logfile = file("/tmp/pe.log", "w")  #function file can be substituded with open
    pe.expect(["ro", "pass", "password", "Password"])
    pe.sendline("%s" % psd)
    pe.readline()
    print "before:\"", pe.before, "\""
    print "after:\"",pe.after, "\""
    pe.expect("#")
    pe.sendline("ls -l /home")
    pe.readline()
    print "before:\"", pe.before, "\""
    print "after:\"",pe.after, "\""
    pe.expect("#")
    pe.sendline("exit")

    ft = open("/tmp/pe.log", 'r')
    while True:
        ct = ft.readline()
        if not ct:
            break
        if "puppet" in ct:
            print ct
    #    print ct
    ft.close()
