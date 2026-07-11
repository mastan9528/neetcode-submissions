class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i , val in enumerate(nums):
            remaining = target - val
            if remaining in dic:
                return [dic[remaining] , i]
            dic[val] = i

        return [] 
        