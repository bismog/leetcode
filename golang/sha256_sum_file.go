package main

import (
    "fmt"
    "log"
    "crypto/sha256"
    "io"
    "os"
    "encoding/hex"
)

func main() {
    f,err := os.Open("/run/abc/hello")
    if err != nil {
        log.Fatal(err)
    }
    defer f.Close()

    h := sha256.New()
    if _,err = io.Copy(h, f); err != nil {
        log.Fatal(err)
    }
    // fmt.Printf("%x\n", h.Sum(nil))
    // fmt.Printf("%s\n", string(h.Sum(nil)))
    fmt.Printf("%s\n", hex.EncodeToString(h.Sum(nil)))
}
