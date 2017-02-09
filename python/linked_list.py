#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Reference: http://www.cnblogs.com/linxiyue/p/3551633.html

class Node(object):
    
    def __init__(self, item):
        self._item = item
        self._next = None

    def _set_item(self, item):
        self._item = item

    def _set_next(self, node):
        self._next = node

    def _get_item(self):
        return self._item

    def _get_next(self):
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

    def _index(self, item):
        if self._is_empty():
            raise NotFound, '%s not found' % item

        count = 0
        cnode = self._head
        while cnode._get_next():
            if cnode._get_item() == item:
                return count
            else:
                cnode = cnode._get_next()
                count += 1
        raise NotFound, '%s not found' % item

    def _search(self, item):
        def _find(self, item):
            return False if not self._index(item) else True
        return _find(item)

    def _remove(self, item):
        try:
            index = self._index(item)
        except NotFound:
            print '%s not found' % item

        count = 0
        pre = None
        cnode = self._head
        while cnode:
            if count == index:
                if not pre:
                    self._head = cnode._get_next()
                else:
                    pre._next = cnode._get_next()
                    # or the same as: pre._set_next(cnode._get_next())
                self._dec_size()
                return True
            else:
                count += 1
                pre = cnode
                cnode = cnode._get_next()

    def _insert(self, item, index = 0):
        inode = Node(item)

        count = 0
        pre = None
        cnode = self._head
        while cnode._get_next():
            if count == index:
                if not pre:
                    self._head = inode
                    self._set_next(cnode)
                else:
                    pre._set_next(inode)
                    inode._set_next(pre._get_next())
                break
            else:
                count += 1
                pre = cnode
                cnode = cnode._get_next()

    def _append(self, item):
        inode = Node(item)
        if self._is_empty():
            self._head = inode
        else:
            cnode = self._head
            while cnode._get_next():
                cnode = cnode._get_next()
            cnode._set_next(inode)



