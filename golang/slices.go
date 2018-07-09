package main

import "fmt"

func main() {
	s := make([]string, 3)
	fmt.Println("emp: ", s)

	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set: ", s)
	fmt.Println("get: ", s[2])
	fmt.Println("len: ", len(s))

	s = append(s, "d")
	s = append(s, "e", "f", "g")
	fmt.Println("apd: ", s)

    s = append(s, "xyz")
    fmt.Println("end: ", s)

	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy: ", c)

	l := s[2:5]
	fmt.Println("sl1: ", l)

	l = s[:5]
	fmt.Println("sl2: ", l)

	l = s[2:]
	fmt.Println("sl3: ", l)

	a := [3]string{"g", "h", "i"}
	fmt.Println("array: ", a)
	t := []string{"g", "h", "i"}
	fmt.Println("slice: ", t)

	twoD := make([][]int, 3	)
	// twoD[2][2] = 33
	// fmt.Println("2d at first: ", twoD)
	for i:=0;i<3;i++ {
		innerLen := i+1
		// twoD[i] = make([]string, innerLen)
		// for j:=0;j<innerLen;j++ {
		// 	twoD[i][j] = "bbb"
		// }
		twoD[i] = make([]int, innerLen)
		for j:=0;j<innerLen;j++ {
			twoD[i][j] = i+j
		}
	}
	fmt.Println("2d: ", twoD)

	// 2d := [][]int{[1], [2,3]}
	// fmt.Println("2d 2:", 2d)
}
