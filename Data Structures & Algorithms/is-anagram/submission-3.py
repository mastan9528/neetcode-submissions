from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = [0] * 26

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            ls[ord(s[i])-97] +=1
            ls[ord(t[i])-97] -=1

        return all(v == 0 for v in ls)
        