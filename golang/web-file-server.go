package main

import (
    "fmt"
    "net/http"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){
        fmt.Fprint(w, "Welcome!\n")
    })

    fs := http.FileServer(http.Dir("xxxx/"))
    http.Handle("/static/", http.StripPrefix("/static/", fs))
    http.ListenAndServe(":8888", nil)
}
