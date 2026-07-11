class Solution:
    def cal_(self , piles , val):
        total = 0
        for x in piles:
            total += math.ceil(x/val)
        return total

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = 0
        for x in piles:
            maxi = max(maxi , x)

        i , j = 1 , maxi
        res = maxi
        while i<=j :
            mid = i + (j-i)//2
            value = self.cal_(piles , mid)
            if value <= h:
                res = mid
                j = mid -1
            else:
                i = mid+1

        return res

            


        