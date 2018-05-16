package main

import "fmt"



type argError struct {
    arg int
    prob string
}

func (e *argError) Error() int {
    fmt.Printf("%d - %s\n", e.arg, e.prob)
    return 0
}


func f2(arg int) int {
    if arg == 42 {
        ae := argError{arg: 5, prob: "good day"}
        // return -1, &argError{arg, "can't work with it"}
        ae.Error()

        // Is this ok?
        &argError{55, "not a good day"}.Error()
        return -1
    }
    return arg+3
}

func main() {
    f2(3)
    f2(42)
}
