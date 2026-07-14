from collections import defaultdict
class Node:
    def __init__(self , key =0, val = 0 , left = None ,right = None):
        self.left = left
        self.key = key
        self.val = val
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = defaultdict()
        self.capacity = capacity

        self.head = None
        self.last = None
        

    def get(self, key: int) -> int:

        if key in self.dic:
            curr = self.dic[key]
            if curr == self.last:
                return self.last.val
            if curr == self.head:
                self.head = curr.right
                if self.head:
                    self.head.left = None
            else:
                curr.left.right = curr.right
                if curr.right:
                    curr.right.left = curr.left
            if self.last:
                self.last.right = curr
            curr.left = self.last
            curr.right=None
            self.last = curr

            if not self.head:
                self.head =curr

            return curr.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            curr = self.dic[key]
            curr.val = value

            if curr ==self.last:
                return

            if curr == self.head:
                self.head = curr.right
                if self.head:
                    self.head.left = None
            else:
                curr.left.right = curr.right
                if curr.right:
                    curr.right.left = curr.left
            if self.last:
                self.last.right = curr
            curr.left = self.last
            curr.right=None
            self.last = curr
            if not self.head:
                self.head = curr
            return
        if self.head is None and self.capacity>0:
            x = Node(key , value)
            self.head = x
            self.last = x
            self.dic[key] = x
        else:
            x = Node(key, value)
            self.last.right = x
            x.left = self.last
            self.last = x
            self.dic[key] = x
            if len(self.dic) >self.capacity:
                if self.head.key in self.dic:
                    del self.dic[self.head.key]
                
                self.head = self.head.right
                if self.head:
                    self.head.left = None

