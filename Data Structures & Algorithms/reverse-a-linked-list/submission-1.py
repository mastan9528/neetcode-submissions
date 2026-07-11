# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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


        