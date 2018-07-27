package main

import "fmt"


func two_sum(nums []int, target int) (int,int) {
    m := make(map[int]int)
    for i:=range(nums) {
        m[nums[i]] = i
    }

    for i:=range(nums) {
        diff := target - nums[i]
        if m[diff] != 0 && m[diff] != i {
            return i, m[diff]
        }
    }
    return 0,0 
}

func main() {
    numbers := []int{1, 3, 8, 4}
    a, b := two_sum(numbers, 11)
    fmt.Printf("%d = %d + %d.\n", 11, numbers[a], numbers[b]) 
}
