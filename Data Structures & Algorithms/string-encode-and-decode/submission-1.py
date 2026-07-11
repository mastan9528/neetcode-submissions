class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            size = len(s)
            st += str(size)
            st +='#'+s

        return st


    def decode(self, s: str) -> List[str]:
        res = []
        i =0
        while i<(len(s)):
            size =""
            while s[i]!='#':
                size +=s[i]
                i +=1
            print(size)
            size = int(size)
            i = i+1
            j = i+size
            res.append(s[i:j])
            i =j

        return res


        
            
