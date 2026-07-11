class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = len(nums) 
        y = len(set(nums))
        return not (x == y)
        