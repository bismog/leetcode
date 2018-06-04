package main

import "os"
import "fmt"
import "encoding/json"

type response1 struct {
    Page int
    Fruit []string
}

type response2 struct {
    Page int  `json:"page"`
    Fruit []string `json:"fruits"`
}

func main() {
    bolB,_ := json.Marshal(true)
    fmt.Println(string(bolB))

    intB,_ := json.Marshal(1)
    fmt.Println(string(intB))

    fltB,_ := json.Marshal(2.34)
    fmt.Println(string(fltB))

    strB,_ := json.Marshal("gopher")
    fmt.Println(string(strB))

    slcD := []string{"apple", "peach", "pear"}
    slcB,_ := json.Marshal(slcD)
    fmt.Println(string(slcB))

    mapD := map[string] int{"apple": 5, "lettuce": 7}
    mapB,_ := json.Marshal(mapD)
    fmt.Println(string(mapB))

    res1D := &response1{
        Page: 1,
        Fruit: []string{"apple", "peach", "pear"}}
    res1B,_ := json.Marshal(res1D)
    fmt.Println(string(res1B))

    res2D := &response2{
        Page: 1,
        Fruit: []string{"apple", "peach", "pear"}}

    res2B,_ := json.Marshal(res2D)
    fmt.Println(string(res2B))

    byt := []byte(`{"num": 6.13, "str": ["a","b"]}`)
    fmt.Println(byt)

    var dat map[string]interface{}
    err := json.Unmarshal(byt, &dat)
    if err != nil {
        panic(err)
    }

    fmt.Println(dat)

    // num := dat["num"]
    // fmt.Println(num.(float64))
    num := dat["num"].(float64)
    fmt.Println(num)

    strs := dat["str"].([]interface{})
    str1 := strs[0].(string)
    fmt.Println(str1)

    str := `{"page": 1, "fruits": ["apple", "peach"]}`
    res := response2{}
    json.Unmarshal([]byte(str), &res)
    fmt.Println(res)
    fmt.Println(res.Fruit[0])

    enc := json.NewEncoder(os.Stdout)
    d := map[string]int{"apple": 5, "lettuce": 7}
    enc.Encode(d)
}
