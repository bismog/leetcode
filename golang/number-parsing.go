package main

import "strconv"
import "fmt"

func main() {
    f,_ := strconv.ParseFloat("1.23", 64)
    fmt.Println(f)

    k,_ := strconv.Atoi("1345")
    fmt.Println(k)
}
