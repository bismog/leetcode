package main

import (
    "fmt"
    "strconv"
)

func main() {
    bint10 := []byte("int (base10): ")
    bint10 = strconv.AppendInt(bint10, -42, 10)
    fmt.Println(string(bint10))

    bint10_2 := strconv.AppendInt(bint10, -42, 2)
    fmt.Println(string(bint10_2))
}
