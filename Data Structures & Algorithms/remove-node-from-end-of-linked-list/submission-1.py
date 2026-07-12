# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        cnt = 0
        while fast !=None and cnt != n:
            fast = fast.next
            cnt +=1
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
        