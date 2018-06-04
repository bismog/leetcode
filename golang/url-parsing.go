package main

import "fmt"
import "net"
import "net/url"

func main() {
    s := "sftp://user:password@gitpush.ml:8964/path/to/file?key=val#f"
    u,_ := url.Parse(s)
    fmt.Println(u.Scheme)

    fmt.Println(u.User)
    fmt.Println(u.User.Username())
    pass,_ := u.User.Password()
    fmt.Println(pass)
    fmt.Println(u.Host)
    host,port,_ := net.SplitHostPort(u.Host)
    fmt.Println(host)
    fmt.Println(port)
    fmt.Println(u.Path)
    fmt.Println(u.Fragment)

    fmt.Println(u.RawQuery)
    m,_ := url.ParseQuery(u.RawQuery)
    fmt.Println(m)
    fmt.Println(m["key"][0])
}
