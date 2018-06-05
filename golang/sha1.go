package main

import "crypto/sha1"
import "fmt"

func main() {
    s := "please calculate me"
    h := sha1.New()

    h.Write([]byte(s))

    bs := h.Sum(nil)
    fmt.Println(s)
    fmt.Printf("%x\n", bs)
}
