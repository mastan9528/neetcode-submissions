class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                if len(stack) >=1:
                    if not ((ch == '}' and stack[-1] == '{') or (ch == ']' and stack[-1] == '[') or (ch == ')' and stack[-1] == '(')):
                        return False
                    else:
                        stack.pop()


                else:
                    return False

        if len(stack) == 0:
            return True
        return False
        