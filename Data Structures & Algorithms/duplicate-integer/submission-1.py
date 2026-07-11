class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # st = set()
        # for i in range(len(nums)):
        #     if nums[i] in st:
        #         return True
        #     st.add(nums[i])

        # return False
        return len(set(nums)) < len(nums)
        
        