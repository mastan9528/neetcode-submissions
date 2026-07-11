from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = defaultdict(int)

        for i in range(len(s)):
            dic1[s[i]] +=1
            dic1[t[i]] -=1

        return all(v==0 for v in dic1.values())
        