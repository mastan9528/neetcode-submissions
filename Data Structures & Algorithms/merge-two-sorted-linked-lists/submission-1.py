# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = ListNode()
        x , y = list1 ,list2
        k = p
        while x!=None and y!=None:
            if x.val <= y.val:
                k.next = x
                k = k.next
                x=x.next
                k.next =None
            else:
                k.next = y
                k = k.next
                y=y.next
                k.next =None

        while x!=None:
            k.next = x
            k = k.next
            x=x.next
            k.next =None
        while y!=None:
            k.next = y
            k = k.next
            y=y.next
            k.next =None
        return p.next

