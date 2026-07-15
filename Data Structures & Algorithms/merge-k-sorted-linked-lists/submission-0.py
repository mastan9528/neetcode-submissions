# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  

    def mergelist(self , left , right):
        k = ListNode()
        r = k
        while left and right:
            if left.val <= right.val:
                r.next = left
                r = r.next
                left = left.next
            else:
                r.next = right
                r = r.next
                right = right.next

        while left:
            r.next = left
            r = r.next
            left = left.next
        while right:
            r.next = right
            r = r.next
            right = right.next
        return k.next


    def divide(self , lists , i , j):
        if i>=j:
            return lists[i]
        split_point = (i+j)//2
        left = self.divide(lists , i , split_point)
        right = self.divide(lists , split_point+1 ,j)

        return self.mergelist(left , right)
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0: return None
        return self.divide(lists , 0 , k - 1)