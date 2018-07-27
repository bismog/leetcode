package main

import "fmt"

func max(a int, b int) int {
    if a < b {
        return b
    }
    return a
}

func add_two_numbers(num_a []int, num_b []int) []int {
    max_len := max(len(num_a), len(num_b))
    out := make([]int, max_len+1)
    up_bit := 0
    for i:=0;i<max_len;i++ {
        sum := num_a[i] + num_b[i] + up_bit
        out[i] = sum % 10
        up_bit = sum / 10
    }
    if up_bit != 0 {
        out[max_len] = up_bit
    }
    return out
}

func main() {
    a := []int{1, 3, 5, 7}
    b := []int{8, 4, 8, 4}
    o := add_two_numbers(a, b)
    fmt.Println(o)
}
