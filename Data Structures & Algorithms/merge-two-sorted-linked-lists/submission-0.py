# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q=list2
        k = ListNode()
        res = k

        while p!=None and q !=None:
            if p.val <= q.val:
                res.next = p
                p=p.next
                res = res.next
                res.next = None
            else:
                res.next = q
                q=q.next
                res = res.next
                res.next = None

        while p!=None:
            res.next = p
            p=p.next
            res = res.next
            res.next = None
        while q!=None:
            res.next = q
            q=q.next
            res = res.next
            res.next = None


        return k.next
