# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:

    def reverse(self , head) -> Optional[ListNode]:
        p = None 
        q=head
        if head == None:
            return head
        r = q.next
        while q.next !=None:
            q.next = p
            p=q
            q=r
            r=r.next
        q.next = p

        return q



    def reorderList(self, head: Optional[ListNode]) -> None:
        le = 0
        p = head
        while p!=None:
            le +=1
            p=p.next
        cnt = math.ceil(le/2)
        p = head
        while p != None and cnt != 1:
            print(f"{p.val}")
            p = p.next
            cnt -=1
        q = p.next
        p.next = None
        p=head
        q = self.reverse(q)
        k = ListNode()
        res = k
        while p!= None or q !=None:
            if p!=None:
                res.next = p
                p=p.next
                res = res.next
                res.next = None
            if q!=None:
                res.next = q
                q=q.next
                res = res.next
                res.next = None

        head = k.next



















