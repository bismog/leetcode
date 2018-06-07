package main

import (
    "fmt"
    "os"
    "os/signal"
    "syscall"
)

func main() {
    sigs := make(chan os.Signal, 1)
    done := make(chan bool, 1)

    // signal.Notify(sigs, syscall.SIGTERM, syscall.SIGINT)
    signal.Notify(sigs, syscall.SIGINT)

    go func() {
        sig :=<-sigs
        fmt.Println()
        fmt.Println(sig)
        done <- true
    }()

    fmt.Println("Awaiting signals")
    <-done
    fmt.Println("exiting")
}
