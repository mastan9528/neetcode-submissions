class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1 , -1 ,-1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if len(stack)==0:
                stack.append([temperatures[i] , i])
                res[i] = 0
            else:
                stack.append((temperatures[i] , i))
                res[i] = stack[-2][1] - stack[-1][1]

        return res