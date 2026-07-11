class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ls = [1] * len(nums)
        product = 1
        for i in range(1, len(nums)):
            product *= nums[i-1]
            ls[i] = product

        product = 1

        for i in range(len(nums)-2, -1 , -1):
            product *= nums[i+1]
            ls[i] *=product
        print(ls)
        return ls
        