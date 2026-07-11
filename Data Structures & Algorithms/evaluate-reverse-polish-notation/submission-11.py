import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = ['*' , '-' , '/' , '+']
        if len(tokens) == 1 and tokens[0] not in operators:
            return int(tokens[0])
        i=0
        while i < len(tokens):
            if tokens[i] not in operators:
                st.append(tokens[i])

            else:
                y = int(st.pop())
                x = int(st.pop())
                print(f"x:{x} , y:{y}")
                if tokens[i] == '*':
                    z = x * y
                    st.append(z)
                    print(f"z:{z}")
                elif tokens[i] == '/':
                    st.append(int(x/y))
                    print(f"last value {st[-1]}")
                elif tokens[i] == '+':
                    st.append(x+y)
                    print(f"last value {st[-1]}")
                else:
                    st.append(x-y)
                    print(f"last value {st[-1]}")

            i +=1

        return int(st[0])


        