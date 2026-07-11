class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in dic:
                return [dic[wanted] , i]
            dic[nums[i]] = i

        return []
        