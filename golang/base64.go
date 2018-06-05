package main

import b64 "encoding/base64"
import "fmt"

func main() {
    data := "abc123@#)$*@()%#)$#)=fs@~"

    eData := b64.StdEncoding.EncodeToString([]byte(data))
    fmt.Println(eData)
    dData,_ := b64.StdEncoding.DecodeString(eData)
    fmt.Println(string(dData))

    uData := b64.URLEncoding.EncodeToString([]byte(data))
    fmt.Println(uData)
    duData,_ := b64.URLEncoding.DecodeString(uData)
    fmt.Println(string(duData))
}
