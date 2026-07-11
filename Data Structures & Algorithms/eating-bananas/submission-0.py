class Solution:

    def calculate(self , piles , mid):
        cnt = 0
        for i in piles:
            cnt += math.ceil(i / mid)
        print(cnt)

        return cnt

        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        ans = j
        while i<=j:
            mid = i + int((j-i) /2)
            if self.calculate(piles , mid) <= h:
                ans = mid
                j = mid -1
            else:
                i = mid+1

        return ans 
        
        

        