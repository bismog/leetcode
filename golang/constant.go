package main

import "fmt"
import "math"

const s string = "constant"

func main() {
	fmt.Println(s)
	const n = 50000000
	const d = 3e20 / n

	// Can not initilize a constant with non-constant value
	// var tt = 444
	// const pp = tt / 4

	fmt.Println(d)
	fmt.Println(int64(d))

	// Can not given new value for a constant
	// d = 666

	fmt.Println(math.Sin(n))
}
