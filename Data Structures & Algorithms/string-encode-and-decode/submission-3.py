class Solution:
    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            x = len(s)
            st = st + str(x) + "#" + s
        return st

    def decode(self, s: str) -> List[str]:
        x = len(s)
        i , j =0 , 0
        li = []
        while i < x:
            while j <x and s[j] != '#':
                j +=1
            val = int(s[i:j])
            y = j+1+val
            if y <= x:
                li.append(s[(j+1):(j+1+val)])
            i = y
            j = i
            
        return li