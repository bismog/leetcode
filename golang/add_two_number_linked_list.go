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

func (list *NodeList) make_node_list(xs []int) {
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

func add_two_numbers(list_a NodeList, list_b NodeList) (list_o NodeList) {
    cur_a := list_a.head
    cur_b := list_b.head
    carry := 0
    for {
        if cur_a == nil && cur_b == nil {
            break
        }else if cur_a == nil {
            cur_a.bit = 0
        }else if cur_b == nil {
            cur_b.bit = 0
        }
        sum := cur_a.bit + cur_b.bit + carry
        bit_plus := sum % 10
        carry = sum / 10
        list_o.append_node(bit_plus)
        cur_a = cur_a.next
        cur_b = cur_b.next
    }
    if carry != 0 {
        list_o.append_node(carry)
    }
    return list_o
}

func main() {
    a := []int{1, 3, 5, 7}
    b := []int{8, 4, 8, 4}

    list_a := NodeList{0, nil}
    list_b := NodeList{0, nil}

    list_a.make_node_list(a)
    list_b.make_node_list(b)
    list_a.show()
    fmt.Println()
    list_b.show()
    fmt.Println()

    list_o := add_two_numbers(list_a, list_b)
    list_o.show()
}
