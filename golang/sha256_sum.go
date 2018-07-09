package main

import (
    "fmt"
    "crypto/sha256"
    _"strconv"
)

func main() {
    h := sha256.New()
    h.Write([]byte("hello bismog"))
    x := h.Sum(nil)
    fmt.Printf("%x\n", x)
    // fmt.Printf("%s\n", string(x))
}
