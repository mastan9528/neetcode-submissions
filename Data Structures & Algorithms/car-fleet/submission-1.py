class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append([position[i] , speed[i]])

        arr = sorted(arr)

        stack = []
        cnt =0

        for i in range(len(arr)-1 , -1,-1):
            val = (target - arr[i][0]) / arr[i][1]
            while stack and stack[-1] < val :
                stack.pop()
                if len(stack) == 0:
                    cnt +=1
            if len(stack) == 0:
                stack.append(val)

        if len(stack) > 0:
            cnt +=1

        return cnt
        