class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = 1

        maxi = 0


        for i in nums:
            Sum = 0
            x = i
            while x in dic:
                Sum +=1
                x -=1
            maxi = max(maxi , Sum)

        return maxi

        