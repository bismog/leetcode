#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference: http://www.cnblogs.com/linxiyue/p/3551633.html

class Node(object):
    
    def __init__(self, item):
        self._item = item
        self._next = None

    def set_item(self, item):
        self._item = item

    def set_next(self, node):
        self._next = node

    def get_item(self):
        return self._item

    def get_next(self):
        return self._next


class LinkedList(object):

    def __init__(self, node = None):
        if not node:
            self._head = None
            self._size = 0
        else:
            self._head = node
            self._size = 1

    def _is_empty(self):
        return self._head == None

    def _inc_size(self):
        self._size += 1

    def _dec_size(self):
        if self._size >= 1:
            self._size -= 1
        self._size = 0

    def index(self, item):
        if self._is_empty():
            raise NotFound, '%s not found' % item

        count = 0
        cnode = self._head
        while cnode.get_next():
            if cnode.get_item() == item:
                return count
            else:
                cnode = cnode.get_next()
                count += 1
        raise NotFound, '%s not found' % item

    def search(self, item):
        def _find(self, item):
            return False if not self.index(item) else True
        return _find(item)

    def remove(self, item):
        try:
            index = self.index(item)
        except NotFound:
            print '%s not found' % item
            return False

        count = 0
        pre = None
        cnode = self._head
        while cnode:
            if count == index:
                if not pre:
                    self._head = cnode.get_next()
                else:
                    pre._next = cnode.get_next()
                    # or the same as: pre.set_next(cnode.get_next())
                self._dec_size()
                return True
            else:
                count += 1
                pre = cnode
                cnode = cnode.get_next()
        return False

    def insert(self, item, index = 0):
        inode = Node(item)

        count = 0
        pre = None
        cnode = self._head
        while cnode.get_next():
            if count == index:
                if not pre:
                    self._head = inode
                    inode.set_next(cnode)
                else:
                    pre.set_next(inode)
                    inode.set_next(pre.get_next())
                self._inc_size()
                return True
            else:
                count += 1
                pre = cnode
                cnode = cnode.get_next()
        return False

    def append(self, item):
        inode = Node(item)
        if self._is_empty():
            self._head = inode
        else:
            cnode = self._head
            while cnode.get_next():
                cnode = cnode.get_next()
            cnode.set_next(inode)

    def list(self):
        out = []
        cnode = self._head
        while cnode:
            out.append(cnode.get_item())
            cnode = cnode.get_next()
        return out

def main():
    xnode = Node(3)
    linked_list = LinkedList(xnode)

    # ynode = Node(4)
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(6)
    # linked_list.remove(5)
    linked_list.insert(2)

    disp = tuple(linked_list.list())
    print disp

if __name__ == "__main__":
    main()
