class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_hash = dict()
        for i in range(len(nums)):
            if target - nums[i] in my_hash:
                return [my_hash[target - nums[i]], i]
            my_hash[nums[i]] = i
        return []
        