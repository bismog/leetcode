package main

import ("fmt"; "math")

type Circle struct {
    r float64
}

type Rectangle struct {
    x1, y1, x2, y2 float64
}


func (c Circle) distance() float64 {
    return 2 * math.Pi * c.r
}

func distance(x1, y1, x2, y2 float64) float64 {
    a := x2 - x1
    b := y2 - y1
    return math.Sqrt(a*a + b*b)
}

func (c Circle) area() float64 {
    return math.Pi * c.r * c.r
}

func (r Rectangle) area() float64 {
    l := distance(r.x1, r.y1, r.x2, r.y1)
    w := distance(r.x1, r.y1, r.x1, r.y2)
    return l*w
}


func main() {
    // cr := new(Circle)
    // rec := new(Rectangle)

    cr := Circle{5}
    rec := Rectangle{0, 0, 10, 10}

    fmt.Println(rec.area())
    fmt.Println(cr.area())
}
