package main

// import "fmt"
// import "math/rand"
// import "sync"
// import "sync/atomic"
// import "time"

import (
    "fmt"
    "math/rand"
    "sync"
    "sync/atomic"
    "time"
)


func main() {
    var state = make(map[int] int)

    var mutex = &sync.Mutex{}

    var readOps uint64
    var writeOps uint64

    for i:=0;i<100;i++ {
        go func() {
            total := 0
            for {
                key := rand.Intn(5)
                mutex.Lock()
                total += state[key]
                mutex.Unlock()
                atomic.AddUint64(&readOps, 1)
                time.Sleep(time.Millisecond)
            }
        }()
    }

    for w:=0;w<10;w++ {
        go func() {
            for {
                key := rand.Intn(5)
                val := rand.Intn(100)
                mutex.Lock()
                state[key] = val
                mutex.Unlock()
                atomic.AddUint64(&writeOps, 1)
                time.Sleep(time.Millisecond)
            }
        }()
    }

    time.Sleep(time.Second)
    
    readOpsFinal := atomic.LoadUint64(&readOps)
    writeOpsFinal := atomic.LoadUint64(&writeOps)
    fmt.Println("readOps: ", readOpsFinal)
    fmt.Println("writeOps: ", writeOpsFinal)

    mutex.Lock()
    fmt.Println("state: ", state)
    mutex.Unlock()
}
