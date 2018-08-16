package main

import "fmt"

func find_longest_substring(raw string) int {

    left, max_len, cur_len := 0,0,0
    char_dict := map[byte]int{}
    for i:=0;i<len(raw);i++ {
        if char_dict[raw[i]] > 0 {
            if char_dict[raw[i]] < left {
                cur_len++
            } else {
                left = char_dict[raw[i]] + 1
                cur_len = i - char_dict[raw[i]] + 1
            }
        } else {
            cur_len++
        }

        if cur_len >= max_len {
            max_len = cur_len
        }
        char_dict[raw[i]] = i
    }
    return max_len
}


func main() {
    raw_string := "abcdcafbkgzjaf"
    max_len := find_longest_substring(raw_string)
    fmt.Printf("cur_len of longest substring is: %d\n" , max_len)
}
