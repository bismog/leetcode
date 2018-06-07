package main

import "syscall"
import "os"
import "os/exec"
import "fmt"

func main() {
    binary,err := exec.LookPath("ls")
    if err != nil {
        panic(err)
    }
    fmt.Println(binary)

    // args := []string{"-a", "-l", "-h"}
    args := []string{"ls", "-a", "-l", "-h"}
    fmt.Println(args)

    env := os.Environ()

    err = syscall.Exec(binary, args, env)
    if err != nil {
        panic(err)
    }
}
