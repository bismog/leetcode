package main

import "os"
import _"strings"
import "fmt"


func main() {
    os.Setenv("FOO", "1")

    fmt.Println("FOO", os.Getenv("FOO"))
    fmt.Println("BAR", os.Getenv("BAR"))

    fmt.Println()

    fmt.Println(os.Environ())

    // for _,e := range os.Environ() {
    //     pair := strings.Split(e, "=")
    //     fmt.Println(pair)
    // }
}
