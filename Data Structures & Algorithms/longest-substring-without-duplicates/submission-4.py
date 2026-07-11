class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i , j = 0 , 0
        dic = {}
        maxi =0
        while j < len(s):
            while i<j and s[j] in dic:
                del dic[s[i]]
                i +=1

            maxi = max(maxi , j-i+1)
            dic[s[j]] =1
            j +=1

        return maxi



        