# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        