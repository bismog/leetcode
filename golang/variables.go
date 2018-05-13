package main

import "fmt"

var sss = "god bless you!"

func main() {

	sss = "god bless me!"
	fmt.Println(sss)

	// Either specify type of not is alternative
	// var a string = "string"   
	var a = "string"
	fmt.Println(a)

	// Default string will be ''
	var aa string
	// For string we can only use double quote, not single quote
	// fmt.Println('aa is ', aa) is in wrong syntax
	fmt.Println("aa is ", aa)

	// var b, c int = 1, 6
	var b, c = 1, 6
	c = 66
	fmt.Println(b+c)

	//float value
	var ff float32 = 32.32
	fmt.Println(ff)

	// var d bool = true
	var d = true
	fmt.Println(d)

	//default bool is false
    var dd bool
	fmt.Println("dd is ", dd)

	// default integer is 0
	var e int
	fmt.Println(e)

	f := "short"
	fmt.Println(f)

	g := 3
	fmt.Println(g)
}
