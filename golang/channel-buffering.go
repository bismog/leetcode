package main
import "fmt"

func main() {
    message := make(chan string, 2)

    message <- "buffer a"
    message <- "buffer b"

    fmt.Println(<-message)
    fmt.Println(<-message)
}
