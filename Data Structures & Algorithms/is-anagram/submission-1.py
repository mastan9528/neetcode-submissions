class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}

        for i in range(len(s)):
            if s[i] not in dic1:
                dic1[s[i]] = 0
            if t[i] not in dic1:
                dic1[t[i]] = 0
            dic1[s[i]] +=1
            dic1[t[i]] -=1

        return all(v==0 for v in dic1.values())
        