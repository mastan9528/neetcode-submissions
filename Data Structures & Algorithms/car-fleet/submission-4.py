class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr:list[tuple] = []

        stack = []

        for i in range(len(speed)):
            arr.append((position[i] , speed[i]))

        arr = sorted(arr , reverse = True)
        res = 0
        for x in arr:
            des = (target - x[0]) / x[1]
            print(des)
            print(f"x[0] : {x[0]}")
            while stack and des > stack[-1]:
                stack.pop()
            if len(stack) == 0:
                res +=1
            stack.append(des)

        return res
            


        
        