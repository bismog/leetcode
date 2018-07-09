package main

import (
    "fmt"
    "strconv"
)

func main() {
    b32 := []byte("float32:")
    b32 = strconv.AppendFloat(b32, 3.1415926535, 'E', -1, 32)
    fmt.Println(string(b32))
}
