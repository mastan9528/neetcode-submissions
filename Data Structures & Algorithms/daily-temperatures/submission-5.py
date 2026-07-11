class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack :list[tuple]=[]

        result = [0]*len(temperatures)
        i = len(temperatures)-1
        while i >= 0:
            while len(monotonic_stack) > 0 and temperatures[i] >= monotonic_stack[-1][0]:
                monotonic_stack.pop()
            if len(monotonic_stack) == 0:
                result[i] = 0
            else:
                result[i] = monotonic_stack[-1][1] - i
            monotonic_stack.append((temperatures[i] , i))
            i -= 1

        return result

        