class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}

        i , j = 0 , 0
        maxi = 0

        while j < len(s):
            if s[j] in dic and dic[s[j]] >= i:
                i = dic[s[j]]+1

            maxi = max(maxi , j-i+1)
            dic[s[j]] = j
            j +=1

        return maxi



        