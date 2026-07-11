class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for x in range(len(temperatures)-1,-1,-1):
            
            while stack and temperatures[x] >= stack[-1][0]:
                stack.pop()
            if not stack:
                res[x] = 0
                stack.append([temperatures[x] , x])
            else:
                res[x] = stack[-1][1]-x
                stack.append([temperatures[x] , x])

        return res
            


        