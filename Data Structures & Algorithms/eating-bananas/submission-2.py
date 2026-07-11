import math
class Solution:

    def helper(self, piles , mid)-> int:
        cnt = 0
        for i in piles:
            cnt += math.ceil(i/mid)

        return cnt


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        mini = maxi
        i , j = 1 , maxi

        while i <= j:
            mid = (i+j)//2
            cnt = self.helper(piles , mid)
            if cnt <= h:
                mini = mid
                j = mid-1
            else:
                i = mid+1

        return mini


        