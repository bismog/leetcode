package main

import "fmt"
import "flag"

func main() {
    wordPtr := flag.String("word", "foo", "a string")

    intPtr := flag.Int("numb", 42, "an int")
    boolPtr := flag.Bool("fork", true, "a bool")

    var svar string
    flag.StringVar(&svar, "svar", "bar", "a string var")

    flag.Parse()

    fmt.Println("word: ", *wordPtr)
    fmt.Println("numb: ", *intPtr)
    fmt.Println("fork: ", *boolPtr)
    fmt.Println("svar: ", svar)
    fmt.Println("tail: ", flag.Args())
}
