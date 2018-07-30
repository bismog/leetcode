package main

import "fmt"

type Node struct {
    bit int
    next *Node
}

type NodeList struct {
    len int
    head *Node
}

func (list *NodeList) append_node(x int) {
    new_node := new(Node)
    new_node.bit = x
    new_node.next = nil
    list.len++

    if list.head == nil {
        list.head = new_node
    } else {
        tail_node := list.tail()
        if tail_node == nil {
            panic(1)
        }
        tail_node.next = new_node
    }
}

// func (list *NodeList) init_list()  {
//     list.len = 0
//     list.head = nil
// }

func (list *NodeList) make_node_list(xs []int) {
    // list.init_list()
    for _,x := range(xs) {
        list.append_node(x)
    }
}

func (list *NodeList) tail() *Node {
    cur := list.head
    for {
        if cur.next == nil {
            return cur
        }
        cur = cur.next
    }
    return nil
}

func (list *NodeList) show() {
    if list.len == 0 {
        fmt.Println("empty list")
    }
    cur := list.head
    for {
        if cur == nil {
            break
        }
        fmt.Println(cur.bit)
        cur = cur.next
    }
}

func main() {
    a := []int{1, 3, 5, 7}
    b := []int{8, 4, 8, 4}

    // var list_a, list_b NodeList = NodeList{0, nil}, NodeList{0, nil}
    list_a := NodeList{0, nil}
    list_b := NodeList{0, nil}

    list_a.make_node_list(a)
    list_b.make_node_list(b)
    list_a.show()
    list_b.show()
}
