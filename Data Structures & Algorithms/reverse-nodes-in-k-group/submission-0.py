# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self , head):
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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        x = ListNode()
        r = x
        slow = head
        fast = head
        while fast is not None:
            cnt = 1
            while fast and cnt<k:
                fast = fast.next
                if fast:
                    cnt +=1
                else:
                    break
            if cnt == k:
                y = fast.next
                fast.next =None
                fast = y
                s = self.reverse(slow)
                r.next = s
                r = slow
                slow = y
            elif slow:
                r.next = slow    
        return x.next



        