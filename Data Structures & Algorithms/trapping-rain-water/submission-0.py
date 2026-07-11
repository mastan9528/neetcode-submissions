class Solution:
    def trap(self, height: List[int]) -> int:
        ls = [0] * len(height)
        ls2 = [0] * len(height)
        maxi = 0
        for i in range(0,len(height)):
            ls[i] = maxi
            maxi = max(maxi , height[i])
        maxi = 0
        for i in range(len(height)-1 , -1, -1):
            ls2[i] = maxi
            maxi = max(maxi , height[i])
        

        res = 0
        for i in range(len(height)):
            res +=  min(ls[i],ls2[i]) - height[i] if (min(ls[i],ls2[i]) - height[i]) > 0 else 0
        return res

        