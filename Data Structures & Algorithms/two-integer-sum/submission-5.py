class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            bal_val = target - nums[i]
            if bal_val in dic:
                return [dic[bal_val] , i]
            dic[nums[i]] = i

        return []

        