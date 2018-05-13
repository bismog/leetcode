package main

import "fmt"
import "time"

func whatami(i interface{}) int {
// whatami := func(i interface{}) {
	switch t := i.(type) {
	case bool:
		fmt.Println("I'm a boot.")
	case int:
		fmt.Println("I'm a integer.")
	default:
		fmt.Println("Don't know type %T\n", t)
	}
	return 0
}

func main() {
	i := 2
	fmt.Print("Write ", i, " as ")

	switch i {
	case 1:
		fmt.Println("one")
	case 2:
		fmt.Println("two")
	case 3:
		fmt.Println("three")
	}

	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("It's the weekend.")
	default:
		fmt.Println("It's the weekday.")
	}

	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}

	// func whatami(i interface{}) {
	whatami := func(i interface{}) {
		switch t := i.(type) {
		case bool:
			fmt.Println("I'm a boot.")
		case int:
			fmt.Println("I'm a integer.")
		default:
			fmt.Println("Don't know type %T\n", t)
		}
    }
	whatami(true)
	whatami(33)
	whatami("goodday")
}
