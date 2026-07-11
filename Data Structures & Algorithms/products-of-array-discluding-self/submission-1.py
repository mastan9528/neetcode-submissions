class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [1] * len(nums)

        for i in range(1,len(nums)):
            product *= nums[i-1]
            res[i] = product
        product = 1
        for i in range(len(nums)-1 , 0 , -1):
            product *= nums[i]
            res[i-1] *= product 
        print(res)
        return res
        