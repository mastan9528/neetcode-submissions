class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inp = ['{' , '[' , '(']
        out = ['}', ']' , ')']
        for ch in s:
            if ch in inp:
                stack.append(ch)
                #print(stack)
            else:
                if len(stack) == 0:
                    return False
                if ch == '}' and stack[-1] == '{':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                    print(stack)
                elif ch == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        