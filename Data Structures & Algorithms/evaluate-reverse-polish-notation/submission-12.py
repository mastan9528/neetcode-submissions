import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ['*' , '-' , '/' , '+']
        # if len(tokens) == 1 and tokens[0] not in operators:
        #     return int(tokens[0])
        i=0
        while i < len(tokens):
            if tokens[i] not in operators:
                st.append(tokens[i])

            else:
                y = int(st.pop())
                x = int(st.pop())
                if tokens[i] == '*':
                    z = x * y
                    st.append(z)
                elif tokens[i] == '/':
                    st.append(int(x/y))
                elif tokens[i] == '+':
                    st.append(x+y)
                else:
                    st.append(x-y)

            i +=1

        return int(st[0])


        