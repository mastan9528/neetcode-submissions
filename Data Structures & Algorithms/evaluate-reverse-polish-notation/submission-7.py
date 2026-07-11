class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '*' or s=='-' or s =='+' or s == '/':
                ch2 = int(stack.pop())
                ch1 = int(stack.pop())
                if s == '*':
                    val = ch1 * ch2
                elif s == '-':
                    val = ch1 - ch2
                elif s == '+':
                    val = ch1 + ch2
                elif s == '/':
                    val = ch1 / ch2
                stack.append(int(val))

            else:
                stack.append(int(s))


        return stack[-1]

        