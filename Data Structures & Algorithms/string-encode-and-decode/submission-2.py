class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + '#' + s

        return st


    def decode(self, s: str) -> List[str]:
        li = []
        i=0
        while i<len(s):
            j = i
            while j<len(s) and s[j] != '#':
                j +=1

            length = int(s[i:j])
            i = j+1
            j = j+1
            li.append(s[i:i+length])
            i +=length 
            print(li)



        return li

