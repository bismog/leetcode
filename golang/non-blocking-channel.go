package main

import "fmt"

func main() {
    messages := make(chan string, 1)
    signals := make(chan bool, 1)

    // messages <- "hello"
    signals <- true
    select {
    case msg := <-messages:
        fmt.Println("received messages", msg)
    default:
        fmt.Println("no messages received")
    }

    msg := "hi"
    select {
    case messages <- msg:
        fmt.Println("sent message", msg)
    default:
        fmt.Println("no message sent")
    }

    select {
    case msg := <- messages:
        fmt.Println("received message", msg)
    case sig := <- signals:
        fmt.Println("received signal", sig)
    default:
        fmt.Println("no activity")
    }
}