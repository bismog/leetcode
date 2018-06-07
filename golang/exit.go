package main

import "fmt"
import "os"
import _"runtime"

func main() {
    defer fmt.Println("Bye")

    // runtime.Goexit()
    os.Exit(3)
}
