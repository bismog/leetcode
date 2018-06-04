package main

import "bytes"
import "fmt"
import "regexp"

func main() {
    match, _ := regexp.MatchString("p([a-z]+)ch", "peach")
    fmt.Println("1: ", match)

    r,_ := regexp.Compile("p([a-z]+)ch")
    fmt.Println("2: ", r.MatchString("peach"))
    fmt.Println("3: ", r.FindString("peach punch"))
    fmt.Println("4: ", r.FindStringIndex("peach punch"))
    fmt.Println("5: ", r.FindStringSubmatch("punch peach"))
    fmt.Println("6: ", r.FindStringSubmatchIndex("peach punch"))
    fmt.Println("7: ", r.FindAllString("peach punch pinch", -1))
    fmt.Println("8: ", r.FindAllStringSubmatchIndex("peach punch pinch", -1))
    fmt.Println("9: ", r.FindAllString("peach punch pinch", 2))
    // fmt.Println("10: ", []byte("peach"))
    fmt.Println("10: ", r.Match([]byte("peach")))

    r = regexp.MustCompile("p([a-z]+)ch")
    fmt.Println("11: ", r)
    fmt.Println("12: ", r.ReplaceAllString("a peach and a punch", "<fruit>"))
    in := []byte("a peach")
    out := r.ReplaceAllFunc(in, bytes.ToUpper)
    fmt.Println("13: ", string(out))
}
