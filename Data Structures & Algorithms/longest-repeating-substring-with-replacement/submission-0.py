class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}

        i , j = 0 , 0
        maxi = 0
        res = 0
        while j < len(s):
            dic[s[j]] = 1 + dic.get(s[j],0)
            maxi = max(maxi , dic[s[j]])
            while  j-i+1 - maxi > k:
                dic[s[i]] -=1
                i +=1
                

            res = max(res , j-i+1)
            j +=1
        return res




        