class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        heights.append(0)
        maxi = 0

        for i , h in enumerate(heights):
            while stack and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] -1
                maxi = max(maxi , height*width)

            stack.append(i)

        heights.pop()
        return maxi
        