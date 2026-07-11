class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i 
            s += "*end word*"
        return s


    def decode(self, s: str) -> List[str]:
        print(s)
        y = s.split("*end word*")
        ls = []
        for x in range(len(y)-1):
            ls.append(y[x])

        return ls

