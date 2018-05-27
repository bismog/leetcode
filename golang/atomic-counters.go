package main

import "fmt"
import "time"
import "sync/atomic"

func main() {
    var ops uint64

    // go func() {
    //     for i:=0;i<50;i++ {
    //     // for  {
    //         atomic.AddUint64(&ops, 1)
    //         time.Sleep(time.Millisecond)
    //     }
    // }()

    // for i:=0;i<10;i++ {
    //     go func() {
    //         atomic.AddUint64(&ops, 1)
    //         time.Sleep(time.Millisecond)
    //     }()
    // }

    // for  {
    for i:=0;i<50;i++ {
        go func() {
            for {
                atomic.AddUint64(&ops, 1)
                time.Sleep(time.Millisecond)
            }
        }()
    }

    time.Sleep(time.Second)

    opsFinal := atomic.LoadUint64(&ops)
    fmt.Println("ops: ", opsFinal)
}
