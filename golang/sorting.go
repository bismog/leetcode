package main

import "fmt"
import "sort"

func main() {
    strs := []string{"Cucumber", "Coconut", "Banana", "Apple"}
    sort.Strings(strs)
    fmt.Println(strs)

    ints := []int{4, 5, 2, 1, 3}
    sort.Ints(ints)
    fmt.Println(ints)

    s := sort.IntsAreSorted(ints)
    fmt.Println("Sorted", s)
}
