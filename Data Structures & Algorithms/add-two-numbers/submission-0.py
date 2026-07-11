# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        p = l1
        q = l2
        while p != None or q != None:
            value = remainder
            if p != None:
                value += p.val
            if q != None:
                value +=q.val
            #print(value)

            in_val = value % 10
            #print(in_val)
            remainder = int(value / 10)
            q.val = in_val
            if p != None:
                p = p.next
            if p != None and q.next == None:
                new_node = ListNode()
                q.next = new_node
            if p == None and q.next == None and remainder != 0:
                new_node = ListNode()
                q.next = new_node
            q = q.next

        return l2
