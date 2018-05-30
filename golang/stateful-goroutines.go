package main

import (
    "fmt"
    "math/rand"
    "sync/atomic"
    "time"
)

type read0 struct {
    key int
    resp chan int
}

type write0 struct {
    key int
    value int
    resp chan bool
}

func main() {
    var readOps uint64
    var writeOps uint64

    read := make(chan *read0)
    write := make(chan *write0)

    go func() {
        var state = make(map[int] int)
        for {
            select {
            case reads := <-read:
                // reads.resp <- state[read.key]
                reads.resp <- state[reads.key]
            case writes := <-write:
                state[writes.key] = writes.value
                writes.resp <- true
            }
        }
    }()

    for i:=0;i<100;i++ {
        go func() {
            for {
                reads := &read0{
                    key: rand.Intn(5),
                    resp: make(chan int) }
                read <- reads
                <-reads.resp
                atomic.AddUint64(&readOps, 1)
                time.Sleep(time.Millisecond) 
            }
        }()
    }

    for w:=0;w<10;w++ {
        go func() {
            for {
                writes := &write0{
                    key: rand.Intn(5),
                    value: rand.Intn(100),
                    resp: make(chan bool) }
                write <- writes
                <-writes.resp
                atomic.AddUint64(&writeOps, 1)
                time.Sleep(time.Millisecond) 
            }
        }()
    }

    time.Sleep(time.Second)

    readOpsFinal := atomic.LoadUint64(&readOps)
    fmt.Println("readOps: ", readOpsFinal)
    writeOpsFinal := atomic.LoadUint64(&writeOps)
    fmt.Println("writeOps: ", writeOpsFinal)

}
