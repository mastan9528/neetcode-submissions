"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        dic = {}

        p = head
        while p!=None:
            new_node = Node(p.val)
            dic[p] = new_node
            p = p.next 

        p = head
        for key , value in dic.items():
            if key.next == None:
                value.next =None
            else:
                value.next = dic[key.next]
            if key.random == None:
                value.random = None
            else:
                value.random = dic[key.random]

        return dic[head]


        