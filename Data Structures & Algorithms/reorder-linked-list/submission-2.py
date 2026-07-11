# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self , head)->ListNode:
        if not head or not head.next:
            return head
        p =None
        q = head
        r = head.next
        print(r.val)
        while q :
            q.next = p
            p = q
            q = r
            if r:
                r=r.next

        return p

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow =slow.next
        p = slow.next
        slow.next =None
        p = self.reverse(p)
        q = head
        k = ListNode()
        x = k
        while p or q:
            if q:
                x.next = q
                x = x.next
                q = q.next
            if p:
                x.next = p
                x = x.next
                p = p.next





        

        
        