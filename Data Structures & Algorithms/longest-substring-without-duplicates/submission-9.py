class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 1
        dic = {}
        dic[s[i]] = i
        maxi = 1
        while j < len(s):
            if s[j] in dic:
                if dic[s[j]]+1 > i:
                    i = dic[s[j]]+1

            maxi = max(maxi , j-i+1)
            dic[s[j]] = j
            j +=1

        return maxi
