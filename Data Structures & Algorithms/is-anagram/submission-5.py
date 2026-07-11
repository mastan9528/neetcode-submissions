class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li1 , li2 = [0]*26 , [0]*26
        for ch in s:
            li1[ord(ch) - ord('a')] +=1
        for ch in t:
            li2[ord(ch) - ord('a')] +=1

        for i in range(26):
            if li1[i] !=li2[i]:
                return False

        return True
        