import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for st in tokens:
            if st == "*" or st == '+' or st == '-' or st == '/':
                print(stack)
                y = stack.pop()
                x = stack.pop()
                if st == '*':
                    z = x * y
                elif st == '-':
                    z = x - y
                elif st == '+':
                    z = x + y
                elif st == '/':
                    z = math.ceil(x / y) if (x/y) < 0 else math.floor (x / y)
                    
                stack.append(z)
            else:
                val = int(st)
                stack.append(val)

        return stack[0]

        