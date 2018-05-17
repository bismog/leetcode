package main

import "fmt"

func main() {
     messages := make(chan string)
 
     go func() { messages <- "ping" }()
 
     msg := <-messages
     fmt.Println(msg)

//    messages := make(chan string, 2)
//    // go func() { messages <- "buf a" }()
//    messages <- "buf a"
//    messages <- "buf b"
//
//    buf_a := <-messages
//    buf_b := <-messages
//
//    fmt.Println(buf_a, buf_b)
}
