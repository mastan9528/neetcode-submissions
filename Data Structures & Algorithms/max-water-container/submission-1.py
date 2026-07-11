class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0

        i , j = 0 , len(heights)-1

        while i<j:
            mini = min(heights[i] , heights[j])
            maxi = max(maxi , (mini * (j-i)))
            if mini == heights[i]:
                i += 1
            else:
                j -=1

        return maxi 
        