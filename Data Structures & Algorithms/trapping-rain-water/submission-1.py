class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = [0] * len(height)
        right_max = [0] * len(height)
        maxi = height[0]
        for i in range(1,len(height)):
            left_max[i] = maxi
            maxi = max(maxi ,height[i])
        maxi = height[len(height)-1]
        for i in range(len(height)-2 , -1 , -1):
            right_max[i] = maxi
            maxi = max(maxi ,height[i])

        ans = 0
        for i in range(len(height)):
            mini = min(left_max[i] , right_max[i])
            if height[i] < mini:
                ans += mini - height[i]


        print(left_max)
        print(right_max)

        return ans

        