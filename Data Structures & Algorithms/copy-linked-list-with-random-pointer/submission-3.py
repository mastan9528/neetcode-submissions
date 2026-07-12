"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        p = head
        node_dic = defaultdict()
        while p:
            node_dic[p] = Node(p.val)
            p = p.next

        for key , valu in node_dic.items():
            valu.next = node_dic.get(key.next)
            valu.random = node_dic.get(key.random)

        return node_dic[head]
        