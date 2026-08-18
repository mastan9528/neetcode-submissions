class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        li1 = [0]*26
        for i in range(len(s)):
            li1[ord(s[i]) - ord('a')] +=1
            li1[ord(t[i]) - ord('a')] -=1

        for i in range(26):
            if li1[i] !=0:
                return False

        return True
        